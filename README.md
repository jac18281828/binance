# binance power toys
# example code for placing orders and listening to the user data stream

```
https://testnet.binance.vision/api/v3/userDataStream
listen key is lU5josyu0Xmpaz0TLLjxxUhJy280HLUFCaK0B60XaXhoiyhtDB5TB1JCmlfU
connect wss://testnet.binance.vision/ws/lU5josyu0Xmpaz0TLLjxxUhJy280HLUFCaK0B60XaXhoiyhtDB5TB1JCmlfU
{"method": "SUBSCRIBE", "id": 1, "params": ["btcusdt@trade", "@balance"]}
{"result":null,"id":1}
{"e":"executionReport","E":1605823200521,"s":"BTCUSDT","c":"daa3Lntyw5phO7yGkmkUzn","S":"BUY","o":"LIMIT","f":"GTC","q":"0.01000000","p":"9000.00000000","P":"0.00000000","F":"0.00000000","g":-1,"C":"","x":"NEW","X":"NEW","r":"NONE","i":339230,"l":"0.00000000","z":"0.00000000","L":"0.00000000","n":"0","N":null,"T":1605823200520,"t":-1,"I":679393,"w":true,"m":false,"M":false,"O":1605823200520,"Z":"0.00000000","Y":"0.00000000","Q":"0.00000000"}
{"e":"outboundAccountInfo","E":1605823200521,"m":0,"t":0,"b":0,"s":0,"T":true,"W":false,"D":false,"u":1605823200520,"B":[{"a":"BNB","f":"1000.00000000","l":"0.00000000"},{"a":"BTC","f":"1.01000000","l":"0.00000000"},{"a":"BUSD","f":"10000.00000000","l":"0.00000000"},{"a":"ETH","f":"100.00000000","l":"0.00000000"},{"a":"LTC","f":"500.00000000","l":"0.00000000"},{"a":"TRX","f":"500000.00000000","l":"0.00000000"},{"a":"USDT","f":"9780.00000000","l":"90.00000000"},{"a":"XRP","f":"50000.00000000","l":"0.00000000"}],"P":["SPOT"]}
{"e":"outboundAccountPosition","E":1605823200521,"u":1605823200520,"B":[{"a":"BTC","f":"1.01000000","l":"0.00000000"},{"a":"USDT","f":"9780.00000000","l":"90.00000000"}]}
{"e":"executionReport","E":1605823228215,"s":"BTCUSDT","c":"R7jZ6w1DPgAo3OFPQDMC0W","S":"BUY","o":"LIMIT","f":"GTC","q":"0.01000000","p":"9000.00000000","P":"0.00000000","F":"0.00000000","g":-1,"C":"daa3Lntyw5phO7yGkmkUzn","x":"CANCELED","X":"CANCELED","r":"NONE","i":339230,"l":"0.00000000","z":"0.00000000","L":"0.00000000","n":"0","N":null,"T":1605823228214,"t":-1,"I":679407,"w":false,"m":false,"M":false,"O":1605823200520,"Z":"0.00000000","Y":"0.00000000","Q":"0.00000000"}
{"e":"outboundAccountInfo","E":1605823228215,"m":0,"t":0,"b":0,"s":0,"T":true,"W":false,"D":false,"u":1605823228214,"B":[{"a":"BNB","f":"1000.00000000","l":"0.00000000"},{"a":"BTC","f":"1.01000000","l":"0.00000000"},{"a":"BUSD","f":"10000.00000000","l":"0.00000000"},{"a":"ETH","f":"100.00000000","l":"0.00000000"},{"a":"LTC","f":"500.00000000","l":"0.00000000"},{"a":"TRX","f":"500000.00000000","l":"0.00000000"},{"a":"USDT","f":"9870.00000000","l":"0.00000000"},{"a":"XRP","f":"50000.00000000","l":"0.00000000"}],"P":["SPOT"]}
{"e":"outboundAccountPosition","E":1605823228215,"u":1605823228214,"B":[{"a":"BTC","f":"1.01000000","l":"0.00000000"},{"a":"USDT","f":"9870.00000000","l":"0.00000000"}]}
```


# place order
```
✔ ~/sandbox/binance [main|●1✚ 4] 
15:57 $ python3 order.py bi_apikey.json 
Order Result = {'symbol': 'BTCUSDT', 'orderId': 339230, 'orderListId': -1, 'clientOrderId': 'daa3Lntyw5phO7yGkmkUzn', 'transactTime': 1605823200520, 'price': '9000.00000000', 'origQty': '0.01000000', 'executedQty': '0.00000000', 'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'BUY', 'fills': []}

```

# cancel order

```
✔ ~/sandbox/binance [main|●1✚ 4] 
16:00 $ python3 cancel_order.py bi_apikey.json 339230
Order Result = b'{"symbol":"BTCUSDT","origClientOrderId":"daa3Lntyw5phO7yGkmkUzn","orderId":339230,"orderListId":-1,"clientOrderId":"R7jZ6w1DPgAo3OFPQDMC0W","price":"9000.00000000","origQty":"0.01000000","executedQty":"0.00000000","cummulativeQuoteQty":"0.00000000","status":"CANCELED","timeInForce":"GTC","type":"LIMIT","side":"BUY"}'
```


