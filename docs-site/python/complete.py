import asyncio
import os
from relayx_py import Realtime

client = Realtime({
  "api_key": '${apiKeys.api_key}',
  "secret": '${apiKeys.secret}'
})

client.init()

def callback_fn(data):
    print(data)

async def on_connected():
  print("Connected to Relay!")

  sent = await client.publish("chat.room1", {
      "user_name": "John Doe",
      "message": "How's it going fam?"
  })

  print(f"Message sent => {sent}")



async def main():
    await client.on("chat.room1", callback_fn)
    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())