import asyncio
import websockets
import aioconsole
import os
import sys

def erase_line():
    # Move the cursor up one line
    sys.stdout.write('\033[F')
    # Erase the entire line
    sys.stdout.write('\033[K')
    sys.stdout.flush()
    
async def receive_messages(websocket):
    try:
        while True:
            message = await websocket.recv()                            
            print("{:<20}".format(message))            
            # Add your logic to handle the incoming message here
    except websockets.ConnectionClosed:
        print("WebSocket connection closed")

async def send_messages(websocket):
    try:
        while True:            
            message = await aioconsole.ainput("")
            erase_line()
            if message == 'exit':
                break

            await websocket.send(message)
            # right align
            terminal_width = os.get_terminal_size().columns
            print(f"{message:>{terminal_width}}")

    except websockets.ConnectionClosed:
        print("WebSocket connection closed")

async def connect_to_websocket():
    async with websockets.connect('ws://localhost:8888/websocket') as websocket:
        print("WebSocket connection established")

        receive_task = asyncio.ensure_future(receive_messages(websocket))
        send_task = asyncio.ensure_future(send_messages(websocket))

        await asyncio.gather(receive_task, send_task)

asyncio.get_event_loop().run_until_complete(connect_to_websocket())