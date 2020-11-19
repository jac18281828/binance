import asyncio
import urllib.request
import websockets
import json
import sys
import time
import traceback
import ssl
import certifi

class BinanceWss:

    API_URL = 'https://testnet.binance.vision/api'    
    WS_URL = 'wss://testnet.binance.vision/ws'

    PRODUCT_ID='BTCUSDT'

    is_running = True

    def __init__(self, listen_key):
        self.update_time = 0
        self.requestId = 1
        self.listen_key = listen_key

    async def send_json(self, websocket, event):
        event_payload = json.dumps(event)
        print(event_payload)
        await websocket.send(event_payload)

    async def ping(self, websocket):
        await websocket.ping()
        await asyncio.sleep(1)

    async def on_subscription(self, websocket, event):
        print(event)
        
    async def on_message(self, websocket, message):
        self.update_time = time.time()
        event_message = json.loads(message)
        print(message)

    async def send_subscription(self, websocket):
        event = {
            'method': 'SUBSCRIBE',
            'id': self.requestId,
            'params': [
                self.PRODUCT_ID.lower() + '@trade',
                '@balance'
            ]
        }
        
        self.requestId = self.requestId + 1

        await self.send_json(websocket, event)


    async def on_open(self, websocket):
        await self.send_subscription(websocket)

    async def heartbeat(self, websocket):
        now = time.time()
        timedelta = now - self.update_time
        if timedelta > 10:
            await self.ping(websocket)
        await asyncio.sleep(1 - timedelta)

    async def receive_message(self, websocket):
        async for message in websocket:
            await self.on_message(websocket, message)

    def on_error(self, err):
        print('Error in websocket connection: {}'.format(err))
        print(traceback.format_exc(err))
        sys.exit(1)

    async def run_event_loop(self):
        try:

            resource = self.WS_URL + '/' + self.listen_key

            print('connect %s' % resource)

            async with websockets.connect(resource) as websocket:
                await self.on_open(websocket)

                while self.is_running:

                    tasks = [
                        asyncio.ensure_future(self.heartbeat(websocket)),
                        asyncio.ensure_future(self.receive_message(websocket))
                    ]

                    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                    for task in pending:
                        task.cancel()
                    
        except Exception as e:
            self.on_error(e)



def listen_key(apikey):

    api_url = BinanceWss.API_URL + '/v3/userDataStream'

    print(api_url)

    request = urllib.request.Request(api_url, method='POST')

    request.add_header('X-MBX-APIKEY', apikey)

    with urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where())) as request_stream:
        listen_key = json.load(request_stream)
        return listen_key['listenKey']
    raise RuntimeException('Unable to fetch listenKey')
    

if __name__ == '__main__':


    if len(sys.argv) > 1:

        apikeyfile = sys.argv[1]
        with open(apikeyfile) as keystream:
            apikey = json.load(keystream)

            stream_key = listen_key(apikey['key'])

            print('listen key is %s' % stream_key)
            
            asioloop = asyncio.get_event_loop()
            try:
                bwss = BinanceWss(stream_key)
                asioloop.run_until_complete(bwss.run_event_loop())
            finally:
                asioloop.close()
    else:
        print('apikeyfile is required.')
        sys.exit(1)
