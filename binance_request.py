import time, base64, hashlib, hmac, urllib.request, urllib.parse, json, ssl, certifi

class binance_request:

    API_URL = 'https://testnet.binance.vision/api'

    def __init__(self, apikey):
        self.apikey = apikey

    def query(self, endpoint, params):

        apikey = self.apikey['key']
        secret = self.apikey['secret']

        otp = self.apikey['passphrase']

        if len(otp) > 0:
            print('passphrase ignored')

        timestamp = str(int(time.time()*1000))

        binance_request = {}

        binance_request['timestamp'] = timestamp

        binance_request.update(params)
            
        post_param = urllib.parse.urlencode(binance_request)

        hash_block = post_param.encode('utf-8')

        decoded_secret = base64.b64decode(secret)

        api_hmac = hmac.new(secret, hash_block, hashlib.sha256).hexdigest()

        api_signature = api_hmac

        resource = self.API_URL + endpoint

        post_data = post_param + '&' + ('signature=%s' % api_signature)

        print(resource)
        print(post_data)

        api_request = urllib.request.Request(resource, data=post_data.encode('utf-8'))
        
        api_request.add_header('X-MBX-APIKEY', apikey)

        request_result = urllib.request.urlopen(api_request, context=ssl.create_default_context(cafile=certifi.where())).read()
        response_payload=json.loads(request_result)

        if 'error' in response_payload and len(response_payload['error']):
            print(response_payload)
            raise Exception('Request failed' + ':'.join(response_payload['error']))

        result = response_payload['result']
        return result


    def fetch(self, endpoint):
        return self.query(endpoint, {})

        
