// Returns a boolean
var subscribed = await client.on("chat.room1", (data) => {
    console.log(data);
})