from relayx_py import Realtime

async def on_connected():
    print("Connected to Relay!")

await client.on(Realtime.CONNECTED, on_connected)