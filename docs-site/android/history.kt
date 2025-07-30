import java.time.Instant
import java.time.temporal.ChronoUnit

val now = Instant.now()

// Set start date to 4 days ago
val startDate: Long = now.minus(4, ChronoUnit.DAYS).toEpochMilli()

// Set end date to 2 days ago 
val endDate: Long = now.minus(2, ChronoUnit.DAYS).toEpochMilli()

val history = client.history("chat.room1", start, end)

// OR

// This will return messages from $start to now()
val history = client.history("chat.room1", start, null)

// --------------------------------------------------------
// $history will look like (an array of JsonObject [com.google.gson.JsonObject])
[
    {
        "id": "<MESSAGE ID>",
        "topic": "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
        "message": <Actual message as string, number or dict>,
        "timestamp": "<Timestamp at which message was sent>"
    }, 
    ...
]