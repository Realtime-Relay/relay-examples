// Returns a boolean
var subscribed = await client.on("chat.room", (data) => {
    console.log("We got a message!")
    console.log(data);
})