import asyncio
import sys
from relayx_py import Realtime

client = Realtime({
  "api_key": '$api_key',
  "secret": '$secret'
})

client.init()

def callback_fn(data):
    print("We got a message!")
    print(data)

    print()
    print("Ctrl + C to quit")

async def on_connected():
    topic = sys.argv[1]

    print("Connected to relayX!")

    print("Listening for messages on topic => {}".format(topic))

    await client.on(topic, callback_fn)

async def main():
    if len(sys.argv) < 3:
        print("Usage: python <file name>.py <topic>")

        print()
        print("Ctrl + C to quit")

    topic = sys.argv[1]

    print("Topic => {}".format(topic))

    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())