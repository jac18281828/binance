from binance_request import binance_request
import json

class binance_order(binance_request):

    def test(self, order):
        result = self.post('/v3/order/test', order)
        return json.loads(result.decode())
    
    def submit(self, order):
        result=self.post('/v3/order', order)
        return json.loads(result.decode())

    def listen_key(self):
        result=self.post('/v3/userDataStream', {})
        return json.loads(result.decode())

    def list(self, order_param):
        return self.fetch('/v3/openOrders', order_param)
    
    def cancel(self, order_param):
        return self.delete('/v3/order', order_param)

    def cancel_open(self, order_param):
        return self.delete('/v3/openOrders', order_param)

    
