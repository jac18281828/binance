import asyncio
import websockets
import json
import sys
import time
import traceback

class BinanceWss:

    WS_URL = 'wss://testnet.binance.vision/ws'

    PRODUCT_ID='BTCUSDT'

    is_running = True

    def __init__(self):
        self.update_time = 0
        self.requestId = 1

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

        if event_message['id'] == '1' and event_message['result'] == None:
            is_running = True
        else:
            is_running = False
        

    async def send_subscription(self, websocket):
        event = {
            'method': 'SUBSCRIBE',
            'id': self.requestId,
            'params': [
                self.PRODUCT_ID.lower() + '@trade'
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
            print('Idle: sending ping')
            await self.ping(websocket)
        else:
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

            async with websockets.connect(self.WS_URL) as websocket:
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

if __name__ == '__main__':

    asioloop = asyncio.get_event_loop()
    try:
        bwss = BinanceWss()
        asioloop.run_until_complete(bwss.run_event_loop())
    finally:
        asioloop.close()

