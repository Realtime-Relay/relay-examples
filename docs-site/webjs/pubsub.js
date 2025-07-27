await client.on("chat.room1", (data) => {
    console.log(data);
})

client.on(Realtime.CONNECTED, async () => {
  console.log("Connected to Relay!")

  var sent = await client.publish("chat.room1", {
      user_name: "John Doe",
      message: "How's it going fam?"
  });

  console.log("Message sent => " + sent);  
})

client.connect()