// Returns a boolean
let subscribe = client.on("chat.room") { payload -> 
  Log.d("Message", payload)
}