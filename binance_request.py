import time, base64, hashlib, hmac, urllib.request, urllib.parse, json, ssl, certifi

class binance_request:

    API_URL = 'https://testnet.binance.vision/api'

    def __init__(self, apikey):
        self.apikey = apikey

    def build(self, params):
        otp = self.apikey['passphrase']

        if len(otp) > 0:
            print('passphrase ignored')

        timestamp = int(time.time()*1000)

        binance_request = {}

        binance_request.update(params)

        binance_request['timestamp'] = timestamp

        return binance_request
    

    def sign(self, hash_block):
        secret = self.apikey['secret']
        
        # using the encoded string as the password!  Rather than the password!
        decoded_secret = secret.encode('utf-8') # base64.b64decode(secret)

        return hmac.new(decoded_secret, hash_block, hashlib.sha256).hexdigest()

    def delete(self, endpoint, params):

        binance_request = self.build(params)
            
        post_param = urllib.parse.urlencode(binance_request)

        hash_block = post_param.encode('utf-8')

        api_signature = self.sign(hash_block)

        resource = self.API_URL + endpoint

        post_data = post_param + '&' + ('signature=%s' % api_signature)

        api_request = urllib.request.Request(resource, data=post_data.encode('utf-8'), method='DELETE')

        apikey = self.apikey['key']
        
        api_request.add_header('X-MBX-APIKEY', apikey)

        with urllib.request.urlopen(api_request, context=ssl.create_default_context(cafile=certifi.where())) as request_stream:
            return request_stream.read()

        raise RuntimeError("Request failed!")


    def post(self, endpoint, params):

        binance_request = self.build(params)
            
        post_param = urllib.parse.urlencode(binance_request)

        hash_block = post_param.encode('utf-8')

        api_signature = self.sign(hash_block)

        resource = self.API_URL + endpoint

        post_data = post_param + '&' + ('signature=%s' % api_signature)

        api_request = urllib.request.Request(resource, data=post_data.encode('utf-8'))

        apikey = self.apikey['key']
        
        api_request.add_header('X-MBX-APIKEY', apikey)

        with urllib.request.urlopen(api_request, context=ssl.create_default_context(cafile=certifi.where())) as request_stream:
            return request_stream.read()

        raise RuntimeError("Request failed!")

    def fetch(self, endpoint, params):
        binance_request = self.build(params)
            
        request_param = urllib.parse.urlencode(binance_request)

        hash_block = request_param.encode('utf-8')

        api_signature = self.sign(hash_block)

        resource = self.API_URL + endpoint

        request_data = request_param + '&' + ('signature=%s' % api_signature)

        api_request = urllib.request.Request(resource + '?' + request_data)

        apikey = self.apikey['key']
        
        api_request.add_header('X-MBX-APIKEY', apikey)

        with urllib.request.urlopen(api_request, context=ssl.create_default_context(cafile=certifi.where())) as request_stream:
            return request_stream.read()

        raise RuntimeError("Request failed!")


        
