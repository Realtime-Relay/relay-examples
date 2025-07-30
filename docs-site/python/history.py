from datetime import datetime, timedelta, UTC

now = datetime.now(UTC)

# Set start date to 4 days ago
start = now - timedelta(days=4)

# Set end date to 2 days ago 
end = now - timedelta(days=2)

history = await client.history("chat.room1", start, end)

# OR

# This will return messages from $start to now()
history = await client.history("chat.room1", start)

# --------------------------------------------------------
# $history will look like
[
    {
        id: "<MESSAGE ID>",
        topic: "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
        message: <Actual message as string, number or dict>,
        timestamp: "<Timestamp at which message was sent>"
    }, 
    ...
]