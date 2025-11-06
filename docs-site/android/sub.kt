client.on("chat.room1") { payload -> 
  Log.d("Message", payload)
}

client.on(Realtime.CONNECTED) {
  Log.d("SDKEvent", "Connected to Relay!")
}