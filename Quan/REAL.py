import pandas as pd
import numpy as np
from binance.client import Client
from datetime import datetime 
import matplotlib.pyplot as plt

# https://medium.com/@andras1000_18467/how-to-run-a-python-script-in-the-cloud-e486eef96ac3

def GetHistoricalData(symbol, interval, fromDate, toDate):
    klines = client.futures_historical_klines(symbol, interval, fromDate, limit = 800)
    df = pd.DataFrame(klines, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
    df['date'] = df.dateTime.dt.strftime("%d/%m/%Y")
    df['time'] = df.dateTime.dt.strftime("%H:%M:%S")
    df = df.drop(['dateTime', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)
    column_names = ["date", "time", "open", "high", "low", "close", "volume"]
    df = df.reindex(columns=column_names)
    return df

api_key = "qyMM3A9HG9aXgWy4FZtYUdZsScwE2g7eLEhB7DKoy0oRvhyWO4I0O3OMNhDuRA1h"
api_secret = "R3JVAGPY352KPDGV"
client = Client(api_key, api_secret)

fromDate = str(datetime.strptime('13/1/2022', '%d/%m/%Y')) # 本地时间，binance 上的时间要比这多8个小时
toDate = str(datetime.strptime('6/2/2022', '%d/%m/%Y'))
symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_30MINUTE
df = GetHistoricalData(symbol, interval, fromDate, toDate)
print(df)

btc_close = df['close']

row = len(btc_close)

ema12 = np.zeros((row))
ema21 = np.zeros((row))
ema26 = np.zeros((row))
ema50 = np.zeros((row))
alpha9 = 2.0 / (9.0 + 1.0)
alpha12 = 2.0 / (12.0 + 1.0)
alpha21 = 2.0 / (21.0 + 1.0)
alpha26 = 2.0 / (26.0 + 1.0)
alpha50 = 2.0 / (50.0 + 1.0)
btc_close = np.zeros((row))

ema_energy = 0
for i in range(row):
    btc_close[i] = df['close'][i]
    if i == 0:
        ema12[i] = btc_close[i]
        ema21[i] = btc_close[i]
        ema26[i] = btc_close[i]
        ema50[i] = btc_close[i]
    else:
        ema12[i] = alpha12 * btc_close[i] + (1 - alpha12) * ema12[i-1]
        ema21[i] = alpha21 * btc_close[i] + (1 - alpha21) * ema21[i-1]
        ema26[i] = alpha26 * btc_close[i] + (1 - alpha26) * ema26[i-1]
        ema50[i] = alpha50 * btc_close[i] + (1 - alpha50) * ema50[i-1]
        
        
macd = ema12 - ema26 # fast - slow, 蓝色线，代表上升
amacd = np.zeros((row)) # 橙色线，代表下降
for i in range(row):
    if i == 0:
        amacd[i] = macd[i]
    else:
        amacd[i] = alpha9 * macd[i] + (1 - alpha9) * macd[i-1]
macd_energy = macd - amacd
macd_energy_acc = np.zeros((row))

for i in range(row):
    if i < 10:
        macd_energy_acc[i] += macd_energy[i]
    else:
        macd_energy_acc[i] = macd_energy_acc[i] + macd_energy[i] - macd_energy[i-10]

plt.figure(num=1,dpi = 1000)
plt.plot(ema21)
plt.plot(ema50)
plt.plot(btc_close)

plt.figure(num = 2,dpi = 1000)
plt.plot(macd)
plt.plot(amacd)

plt.figure(num=3,dpi = 1000)
plt.plot(macd_energy)
plt.plot(macd_energy_acc)

# simulate
account_balance = 0
btc_num = 0
btc_price = 0
account_status = 0 # 0: None 1:做多 2:做空
account_cutProfit = 0
account_cutLoss = 0
trade_times = 0



for i in range(50,row):
    if account_status == 1:
        btc_curPrice = btc_close[i-1]
        if btc_curPrice > account_cutProfit or btc_curPrice < account_cutLoss:
            account_status = 0
            account_balance += (btc_curPrice - btc_price) / btc_curPrice
            trade_times += 1
        continue
    
    if account_status == 2:
        btc_curPrice = btc_close[i-1]
        if btc_curPrice < account_cutProfit or btc_curPrice > account_cutLoss:
            account_status = 0
            account_balance -= (btc_curPrice - btc_price) / btc_curPrice
            trade_times += 1
        continue
    
    if macd_energy[i] > 0  and macd_energy[i-1] < 0 and ema21[i] > ema50[i] and account_status == 0 and macd_energy_acc[i] > 0:
        account_status = 1
        account_cutProfit = btc_close[i-1] * 1.05
        account_cutLoss = btc_close[i-1]*0.95
        btc_price = btc_close[i-1]
        trade_times += 1
        
    if macd_energy[i] < 0  and macd_energy[i-1] > 0 and ema21[i] < ema50[i] and account_status == 0 and macd_energy_acc[i] < 0:
        account_status = 2
        account_cutProfit = btc_close[i-1] * 0.95
        account_cutLoss = btc_close[i-1]*1.05
        btc_price = btc_close[i-1]
        trade_times += 1
        
