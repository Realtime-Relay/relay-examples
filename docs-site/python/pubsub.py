def callback_fn(data):
    print(data)

def on_connected():
  print("Connected to Relay!")

  sent = await client.publish("chat.room1", {
      "user_name": "John Doe",
      "message": "How's it going fam?"
  })

  print(f"Message sent => {sent}")

await client.on("chat.room1", callback_fn)
await client.on(Realtime.CONNECTED, on_connected)

client.connect()