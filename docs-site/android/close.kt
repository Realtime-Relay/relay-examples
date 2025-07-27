client.on("chat.room1") { payload -> 
  Log.d("Message", payload)
}

client.on("CONNECTED") {
  // ... Code from previous step

  val unsubscribed = client.off("chat.room1")
  Log.d("SDKEvent", "Unsubscribed from chat.room1 => $unsubscribed")

  client.close()
}
                      
client.connect()