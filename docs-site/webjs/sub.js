await client.on("chat.room1", (data) => {
    console.log(data);
})

client.on(CONNECTED, async () => {
  console.log("Connected to Relay!")
})