// Returns a boolean
var subscribed = await client.on("chat.room1", (data) => {
    console.log(data);
})

// -------------------------------------------------
// $data is a json
{
    id: "<MESSAGE ID>",
    topic: "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
    data: <Actual message as string, number or json>
}