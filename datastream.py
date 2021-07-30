import logging
from kiteconnect import KiteTicker
logging.basicConfig(level=logging.DEBUG)

kite_api_key = "9d0gkan3mpw88evk"

with open('access_token.txt', 'r') as f:
    access_token = f.read()

kws = KiteTicker(kite_api_key, access_token)

def on_ticks(ws, ticks):
    # print(ticks[0]['last_price'])
   tlen = len(ticks)
   for i in range(tlen):
       print(ticks[i])
       print()
   print()
   print('===================')
   print()

   print(ticks[0]['last_price'])


def on_connect(ws, response):
    ws.subscribe([9917954])
    ws.set_mode(ws.MODE_FULL, [9917954])

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()
