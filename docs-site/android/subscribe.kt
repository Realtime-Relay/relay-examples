// Returns a boolean
let subscribe = client.on("chat.room1") { payload -> 
  Log.d("Message", payload)
}

// -------------------------------------------------
// $payload will be a JsonObject [com.google.gson.JsonObject]
{
    "id": "<MESSAGE ID>",
    "topic": "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
    "data": <Actual message as string, number or json>
}