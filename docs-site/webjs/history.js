var now = new Date();

// Set start date to 4 days ago
var past = start.setDate(now.getDate() - 4)
var startDate = new Date(past)

// Set end date to 2 days ago 
var past = end.setDate(now.getDate() - 2)
var endDate = new Date(past)

var history = await client.history("chat.room1", startDate, endDate)

// OR

// This will return messages from $startDate to now()
var history = await client.history("chat.room1", startDate)

//--------------------------------------------------------
// $history is a json array
[
    {
        id: "<MESSAGE ID>",
        topic: "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
        message: <Actual message as string, number or json>,
        timestamp: "<Timestamp at which message was sent>"
    }, 
    ...
]