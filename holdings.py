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

# Place an order
# try:
#     order_id = kite.place_order(tradingsymbol="INFY",
#                                 exchange=kite.EXCHANGE_NSE,
#                                 transaction_type=kite.TRANSACTION_TYPE_BUY,
#                                 quantity=1,
#                                 order_type=kite.ORDER_TYPE_MARKET,
#                                 product=kite.PRODUCT_NRML)
#
#     logging.info("Order placed. ID is: {}".format(order_id))
# except Exception as e:
#     logging.info("Order placement failed: {}".format(e.message))

#Imitating sell order placed
#Place_sell_order

#Check for sell order execution (Through kite.orders() and kite.positions())

#Add 2 buy orders to required_orders


print("Start")

#Get all open positions on the account : convert to dataframe
current_positions = pd.DataFrame.from_dict(kite.positions()['net'])
print(current_positions)

buy_order_profit = {'tradingsymbol':'BANKNIFTY2180537000CE', 'price':1, 'trigger_price':0, 'order_type':'LIMIT', 'quantity':25}
buy_order_stoploss = {'tradingsymbol':'BANKNIFTY2180537000CE', 'price':30, 'trigger_price':30, 'order_type':'SL-M', 'quantity':25}
# buy_order_extra = {'tradingsymbol':'BANKNIFTY2180537000CE', 'price':30, 'trigger_price':50, 'order_type':'SL-M', 'quantity':25}
# print(buy_order_profit)
required_buy_orders = pd.DataFrame.from_records([buy_order_profit, buy_order_stoploss])
print("Required", required_buy_orders)

orders = pd.DataFrame.from_dict(kite.orders())
print(kite.orders())
open_buy_orders = orders.loc[(orders['transaction_type'] == 'BUY') & (orders['status'] != 'COMPLETE')]
# open_buy_orders = pd.DataFrame.from_records([buy_order_profit, buy_order_stoploss])
print("Open", open_buy_orders.loc[1,:])

def check_orders(required_buy_orders, open_buy_orders):
    temp_required_buy_orders = required_buy_orders
    temp_open_buy_orders = open_buy_orders
    for index, row in temp_required_buy_orders.iterrows():
        matching_order = temp_open_buy_orders.loc[(temp_open_buy_orders['tradingsymbol'] == row['tradingsymbol']) & ((temp_open_buy_orders['price'] == row['price']) | ((temp_open_buy_orders['trigger_price'] == row['trigger_price']) & (temp_open_buy_orders['trigger_price'] != 0))) & (temp_open_buy_orders['order_type'] == row['order_type']) &(temp_open_buy_orders['quantity'] == row['quantity'])]
        if not matching_order.empty:
            print(matching_order)
            temp_required_buy_orders.drop(index, inplace=True)
            temp_open_buy_orders.drop(index = matching_order.index[0], inplace=True)
    if not temp_required_buy_orders.empty:
        print("Order missing!")
    if not temp_open_buy_orders.empty:
        print("Order extra!")

check_orders(required_buy_orders, open_buy_orders)
#Getting Good till Triggered orders
# gtt_orders = pd.DataFrame.from_dict(kite.get_gtts())
# print(kite.get_gtts())
# open_gtt_orders = orders.loc[(orders['transaction_type'] == 'BUY') & (orders['status'] != 'COMPLETE')]

# if open_buy_orders.shape[0] % 2 != 0:
#     print("Error raised")
#
# print(orders)
# required_orders =

# print(kite.ltp(['NFO:BANKNIFTY2180537000CE']))

print("End")


# # Fetch all orders
# kite.orders()
