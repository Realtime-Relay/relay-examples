import asyncio
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

    text = ""

    loop = asyncio.get_event_loop()

    while text != "exit":
        text = await loop.run_in_executor(None, input, "Enter Message: ")

        if text == "exit":
            unsubscribed = await client.off("$topic")
            print(f"Unsubscribed from $topic => {unsubscribed}")

            await client.close()

            return

        sent = await client.publish("$topic", {
            "user_name": "John Doe",
            "message": "How's it going fam?"
        })

        print(f"Message sent => {sent}")

    

async def main():
    await client.on("$topic", callback_fn)
    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())