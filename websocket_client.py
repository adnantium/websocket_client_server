#!/usr/bin/env python

import asyncio
import random
import websockets

async def handle_message():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        msg = 'Please send me a number...'
        print(f'Sending [{msg}] to connection [{id(websocket)}]')
        await websocket.send(msg)
        while True:
            got_back = await websocket.recv()
            print(f"Got: {got_back}")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(handle_message())
except websockets.exceptions.ConnectionClosedError as cce:
    print('Connection closed!')
except KeyboardInterrupt as ki:
    print('Ending...')
    print(ki)
finally:
    loop.close()


