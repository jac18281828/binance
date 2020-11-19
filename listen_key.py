from binance_order import binance_order

import json,sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            apikeyfile = sys.argv[1]
            with open(apikeyfile) as keyfile:
                apikey = json.load(keyfile)
                orderapi = binance_order(apikey)

                listen_key = orderapi.listen_key()

                print("Result = %s" % orderinfo)
        except Exception as e:
            print("Failed. "+repr(e))
    else:
        print('apikey is required')
