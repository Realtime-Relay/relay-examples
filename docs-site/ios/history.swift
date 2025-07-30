let now = Date()

// Set start date to 4 days ago
let startDate = now.addingTimeInterval(-4 * 24 * 60 * 60)

// Set end date to 2 days ago 
let endDate = now.addingTimeInterval(-2 * 24 * 60 * 60)

let history = try await client.history(
    topic: "chat.room1",
    start: startDate,
    end: endDate
)

// OR

// This will return messages from $startDate to now()
let history = try await client.history(
    topic: "chat.room1",
    start: startDate
)

// --------------------------------------------------------
// $history will look like
[
    [
        id: "<MESSAGE ID>",
        topic: "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
        message: <Actual message as string, number or dict>,
        timestamp: "<Timestamp at which message was sent>"
    ], 
    ...
]
