import asyncio
import os
from relayx_py import Realtime

client = Realtime({
  "api_key": '$api_key',
  "secret": '$secret'
})

client.init()

def callback_fn(data):
    print(data)

async def on_connected():
    print("Connected to Relay!")

    sent = await client.publish("$topic", {
        "user_name": "John Doe",
        "message": "How's it going fam?"
    })

    print(f"Message sent => {sent}")

    unsubscribed = await client.off("$topic")
    print(f"Unsubscribed from $topic => {unsubscribed}")

    await client.close()

async def main():
    await client.on("$topic", callback_fn)
    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())