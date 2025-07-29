from relayx_py import Realtime

async def on_disconnect():
    print("Disconnect from Relay")

await client.on(Realtime.DISCONNECTED, on_disconnect)