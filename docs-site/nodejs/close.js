await client.on("chat.room1", (data) => {
    console.log(data);
})

client.on(Realtime.CONNECTED, async () => {
  // ... Code from previous step

  var unsubscribed = await client.off("chat.room1")
  console.log("Unsubscribed from chat.room1 => " + unsubscribed)

  await client.close()
})

client.connect()