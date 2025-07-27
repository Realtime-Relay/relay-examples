client.on("chat.room1") { payload -> 
  Log.d("Message", payload)
}

client.on("CONNECTED") {
  Log.d("SDKEvent", "Connected to Relay!")

  val message = buildMap<String, Any> {
      put("user_name", "John Doe")
      put("message", "How's it going fam?")
  }

  val sent = client.publish("chat.room1", message)
  Log.d("Message", "Message sent => $sent")
}
                      
client.connect()