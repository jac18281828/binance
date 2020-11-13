from binance_request import binance_request


class binance_order(binance_request):


    def test(self, order):
        return self.query('/v3/order/test', order)

    
    def submit(self, order):
        return self.query('/v3/order', order)

