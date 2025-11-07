// Returns a boolean
let subscribe = client.on("chat.room1") { payload -> 
  Log.d("Message", payload)
}