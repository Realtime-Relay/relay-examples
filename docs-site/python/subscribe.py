def callback_fn(data):
    print(data)

# Returns a boolean
subscribed = await client.on("chat.room1", callback_fn)