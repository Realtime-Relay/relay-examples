sent = await client.publish("<YOUR TOPIC>", {
    "user_name": "John Doe",
    "message": "How's it going fam?"
})

sent = await client.publish("<YOUR TOPIC>", "String messages are valid!")

# So are numbers
sent = await client.publish("<YOUR TOPIC>", 1234);

sent = await client.publish("<YOUR TOPIC>", 1234.231);