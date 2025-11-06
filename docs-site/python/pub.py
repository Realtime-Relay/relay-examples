"""
* publish() returns a boolean
* Returns true if message was published
* Returns false if message was not published
"""
sent = await client.publish("chat.room1", {
    "user_name": "John Doe",
    "message": "How's it going fam?"
})

print(f"Message sent => {sent}")