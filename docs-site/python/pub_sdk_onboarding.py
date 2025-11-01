sent = await client.publish("chat.room", "Hello world!")

print(f"Message sent => {sent}")