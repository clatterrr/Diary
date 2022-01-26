import os
import time
import traceback

import pandas as pd
from selenium import webdriver

import utils

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://fund.10jqka.com.cn/datacenter/sy/")
time.sleep(10)
driver.find_element_by_xpath('//tr[@class="tr_hover"]').text.split()
columns = [
    '序号',
    '基金代码',
    '基金名称',
    '相关链接',
    '更新日期',
    '周收益',
    '月收益',
    '季收益',
    '年收益',
    '三年收益',
    '今日收益',
    '成立以来收益率',
    '操作'
]

# 股票型
driver.find_element_by_xpath('//dd[@type="gpx"]').click()
time.sleep(5)

# 年收益排序
driver.find_element_by_xpath('//span[@sort="F011"]').click()
time.sleep(5)

for i in range(10):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(5)
else:

    js = 'var q=document.documentElement.scrollTop=0'
    driver.execute_script(js)
    time.sleep(5)

eles = driver.find_elements_by_xpath('//tbody[@id="containerMain"]/tr')

res = []
for ele in eles:
    res.append(ele.text.split())

res = pd.DataFrame(data=res, columns=columns)
res.drop(columns=['相关链接', '今日收益', '操作'], inplace=True)

res.to_excel('raw_data/股票型基金.xlsx', header=True, index=False)

# 混合型
driver.find_element_by_xpath('//dd[@type="hhx"]').click()
time.sleep(5)

# 年收益排序
driver.find_element_by_xpath('//span[@sort="F011"]').click()
time.sleep(5)

for i in range(10):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(5)

else:
    js = 'var q=document.documentElement.scrollTop=0'
    driver.execute_script(js)
    time.sleep(5)

eles = driver.find_elements_by_xpath('//tbody[@id="containerMain"]/tr')

res = []
for ele in eles:
    res.append(ele.text.split())

res = pd.DataFrame(data=res, columns=columns)
res.drop(columns=['相关链接', '今日收益', '操作'], inplace=True)

res.to_excel('raw_data/混合型基金.xlsx', header=True, index=False)

# 股票型
driver.find_element_by_xpath('//dd[@type="gpx"]').click()
time.sleep(5)
# 年收益排序
driver.find_element_by_xpath('//span[@sort="F011"]').click()
time.sleep(5)

for i in range(10):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(5)
else:
    js = 'var q=document.documentElement.scrollTop=0'
    driver.execute_script(js)
    time.sleep(5)

eles = driver.find_elements_by_xpath('//td[@class="links_td links_val"]/a')

for ele in eles[1:]:
    try:
        name = ele.get_attribute('text')
        href = ele.get_attribute('href')
        utils.get_top10_list(name, href)
    except Exception:

        traceback.print_exc()


# 混合型
driver.find_element_by_xpath('//dd[@type="hhx"]').click()
time.sleep(5)

# 年收益排序
driver.find_element_by_xpath('//span[@sort="F011"]').click()
time.sleep(5)

for i in range(10):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(5)
else:
    js = 'var q=document.documentElement.scrollTop=0'
    driver.execute_script(js)
    time.sleep(5)

eles = driver.find_elements_by_xpath('//td[@class="links_td links_val"]/a')

for ele in eles[1:]:
    try:
        name = ele.get_attribute('text')
        href = ele.get_attribute('href')
        utils.get_top10_list(name, href)
    except Exception:
        traceback.print_exc()
