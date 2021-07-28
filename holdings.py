import logging
from kiteconnect import KiteConnect
from flask import Flask, request, jsonify, session
import os
import json
from datetime import date, datetime
from decimal import Decimal

logging.basicConfig(level=logging.DEBUG)

kite_api_key = "9d0gkan3mpw88evk"

kite = KiteConnect(api_key=kite_api_key)

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

with open('access_token.txt', 'r') as f:
    access_token = f.read()


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

print("Start")
print(kite.holdings())
print("End")
# # Fetch all orders
# kite.orders()
#
# # Get instruments
# kite.instruments()
#
# # Place an mutual fund order
# kite.place_mf_order(
#     tradingsymbol="INF090I01239",
#     transaction_type=kite.TRANSACTION_TYPE_BUY,
#     amount=5000,
#     tag="mytag"
# )
#
# # Cancel a mutual fund order
# kite.cancel_mf_order(order_id="order_id")
#
# # Get mutual fund instruments
# kite.mf_instruments()
