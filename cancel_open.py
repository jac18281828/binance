from binance_order import binance_order
import sys,time,json

if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            apikeyfile = sys.argv[1]
            with open(apikeyfile) as keyfile:
                apikey = json.load(keyfile)
                orderapi = binance_order(apikey)

                order_param = {
                    'symbol': 'BTCUSDT',
                    'timestamp': int(time.time()-86400),
                }

                orderinfo = orderapi.cancel_open(order_param)

                print("Order Result = %s" % orderinfo)
        except Exception as e:
            print("Failed. "+str(e))
    else:
        print('apikey is required')
