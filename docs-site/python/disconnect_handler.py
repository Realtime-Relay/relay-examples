from relayx_py import Realtime

async def on_disconnect():
    print("Connection to Relay closed")

await client.on(Realtime.DISCONNECTED, on_disconnect)