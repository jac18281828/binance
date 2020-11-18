from binance_order import binance_order

import json,sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            apikeyfile = sys.argv[1]
            with open(apikeyfile) as keyfile:
                apikey = json.load(keyfile)
                orderapi = binance_order(apikey)

                order_param = {
                    'symbol': 'BTCUSDT',
                    'orderId': 317834,
                    'timestamp': 1600000000,
                }

                orderinfo = orderapi.list(order_param)

                print("Order Result = %s" % orderinfo)
        except Exception as e:
            print("Failed. "+str(e))
    else:
        print('apikey is required')
