from relayx_py import Realtime

async def on_reconnect(status):
    if status == "RECONNECTING":
        print("Looks like we're not connected, attempting to reconnect to Relay...")
    elif status == "RECONNECTED":
        print("Reconnected to Relay! :D")
    elif status == "RECONN_FAIL":
        print("Failed to reconnect to Relay :(")

await client.on(Realtime.RECONNECT, on_reconnect)