def callback_fn(data):
    print("We got a message!")
    print(data)

def on_connected():
  print("Connected to Relay!")

await client.on("chat.room1", callback_fn)
await client.on(Realtime.CONNECTED, on_connected)