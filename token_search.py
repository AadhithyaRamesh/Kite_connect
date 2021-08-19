import logging
from kiteconnect import KiteConnect
from flask import Flask, request, jsonify, session
import os
import json
from datetime import date, datetime
from decimal import Decimal

import pandas as pd

def token_search(instruments):

    logging.basicConfig(level=logging.DEBUG)
    
    instruments = pd.DataFrame.from_records(kite.instruments())
    
    intrument_token = {}
    
    for inst in instruments:
        
        
        instrument_token[inst] = instruments.loc[(instruments['tradingsymbol'] == inst)].instrument_token.values[0]
    
    return (instrument_token)
