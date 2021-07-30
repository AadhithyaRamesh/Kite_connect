import logging
from kiteconnect import KiteConnect
from flask import Flask, request, jsonify, session
import os
import json
from datetime import date, datetime
from decimal import Decimal

import pandas as pd

logging.basicConfig(level=logging.DEBUG)

kite_api_key = "9d0gkan3mpw88evk"

#Initialise KiteConnect instance
kite = KiteConnect(api_key=kite_api_key)

#Read access token from file.
with open('access_token.txt', 'r') as f:
    access_token = f.read()

#Set access token to KiteConnect instance.
kite.set_access_token(access_token)

instruments = pd.DataFrame.from_records(kite.instruments())

instrument_token = instruments.loc[(instruments['tradingsymbol'] == 'BANKNIFTY2180537000CE')].instrument_token.values[0]

print(instrument_token)
