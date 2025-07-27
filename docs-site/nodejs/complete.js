import Realtime from "relayx-js"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

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

  var unsubscribed = await client.off("chat.room1")
  console.log("Unsubscribed from chat.room1 => " + unsubscribed)

  await client.close()
})

client.connect()