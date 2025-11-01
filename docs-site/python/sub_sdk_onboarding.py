def callback_fn(data):
    print("We got a message!")
    print(data)

# Returns a boolean
subscribed = await client.on("chat.room", callback_fn)