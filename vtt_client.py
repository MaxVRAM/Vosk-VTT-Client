
import asyncio, websockets, argparse, json, sys

from pyaudio import PyAudio, Stream, paInt16
from contextlib import asynccontextmanager, contextmanager, AsyncExitStack
from typing import AsyncGenerator, Generator

from pythonosc import udp_client

# Argument parser config
parser = argparse.ArgumentParser(description='This script creates a WebSocket connection with a Vosk VTT server and outputs the results via OSC.')

parser.add_argument('-server', type=str, default='localhost:2700',
                    help='VTT server <URL:PORT>. Defaults to "localhost:2700". A remote server might look like this: example-server.com:8089')
parser.add_argument('-ip', type=str, default='localhost',
                    help='IP address of the OSC listener. Defaults to "localhost"')
parser.add_argument('-port', type=int, default=9600,
                    help='Port number of the OSC listener. Defaults to 9600')

args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

@contextmanager
def _pyaudio() -> Generator[PyAudio, None, None]:
    p = PyAudio()
    try:
        yield p
    finally:
        print('Terminating PyAudio object')
        p.terminate()

@contextmanager
def _pyaudio_open_stream(p: PyAudio, *args, **kwargs) -> Generator[Stream, None, None]:
    s = p.open(*args, **kwargs)
    try:
        yield s
    finally:
        print('Closing PyAudio Stream')
        s.close()

@asynccontextmanager
async def _polite_websocket(ws: websockets.WebSocketClientProtocol) -> AsyncGenerator[websockets.WebSocketClientProtocol, None]:
    try:
        yield ws
    finally:
        print('Terminating connection')
        await ws.send('{"eof" : 1}')
        print(await ws.recv())

async def run_test(uri):
    async with AsyncExitStack() as stack:
        ws = await stack.enter_async_context(websockets.connect(uri))
        print(f'Connected to {uri}')
        print('Type Ctrl-C to exit')
        ws = await stack.enter_async_context(_polite_websocket(ws))
        p = stack.enter_context(_pyaudio())
        s = stack.enter_context(_pyaudio_open_stream(p,
            format = paInt16, 
            channels = 1,
            rate = 8000,
            input = True, 
            frames_per_buffer = 8000))
        while True:
            data = s.read(8000)
            if len(data) == 0:
                break
            await ws.send(data)

            response = json.loads(await ws.recv())

            if 'partial' in response and len(response['partial']) > 0 and response['partial'] != 'the':
                print(response)
                client.send_message('/partial', '"' + response['partial'] + '"')
            elif 'text' in response and len(response['text']) > 0 and response['text'] != 'the':
                print()
                print(response)
                print()
                client.send_message('/result', '"' + response['text'] + '"') 


try:
    print('Connecting to ws://' + args.vtt_server)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        run_test('ws://' + args.vtt_server))
except (Exception, KeyboardInterrupt) as e:
    loop.stop()
    loop.run_until_complete(
        loop.shutdown_asyncgens())
    if isinstance(e, KeyboardInterrupt):
        print('Bye')
        exit(0)
    else:
        print(f'Oops! {e}')
        exit(1)
