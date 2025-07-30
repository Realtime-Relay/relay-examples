def callback_fn(data):
    print(data)

# Returns a boolean
subscribed = await client.on("chat.room1", callback_fn)

# -------------------------------------------------
# $data is a dict
{
    "id": "<MESSAGE ID>",
    "topic": "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
    "data": <Actual message as string, number or json>
}