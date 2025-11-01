import asyncio
import sys
from relayx_py import Realtime

client = Realtime({
  "api_key": '$api_key',
  "secret": '$secret'
})

client.init()

async def on_connected():
    topic = sys.argv[1]
    message = sys.argv[2]

    print("Connected to relayX!")

    print("Sending message to topic => {}".format(topic))
    print()

    sent = await client.publish(topic, message)

    print(f"Message sent => {sent}")

    print()
    print("Ctrl + C to quit")

async def main():
    if len(sys.argv) < 3:
        print("Usage: python <file name>.py <topic> <message>")

        print()
        print("Ctrl + C to quit")

    topic = sys.argv[1]
    message = sys.argv[2]

    print("Topic => {}".format(topic))
    print("Message => {}".format(message))

    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())