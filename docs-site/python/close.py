def callback_fn(data):
    print(data)

async def on_connected():
  # ... Code from previous step

  unsubscribed = await client.off("chat.room1")
  print(f"Unsubscribed from chat.room1 => {unsubscribed}")

  await client.close()

await client.on("chat.room1", callback_fn)
await client.on(Realtime.CONNECTED, on_connected)

client.connect()