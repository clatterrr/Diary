
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
import pandas as pd
import urllib
import hmac
import requests, json, time, hashlib

api_key = "qyMM3A9HG9aXgWy4FZtYUdZsScwE2g7eLEhB7DKoy0oRvhyWO4I0O3OMNhDuRA1h"
api_secret = "R3JVAGPY352KPDGV"

client = Client(api_key,api_secret);

info = client.get_account()