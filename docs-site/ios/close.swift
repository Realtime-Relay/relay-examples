private class ChatMessageListener: MessageListener {
        
    func onMessage(_ data: Any) {
      print("We got a message!")
      print(data)
    }
}

private class SDKEventListener: MessageListener {
        
    func onMessage(_ data: Any) {
      // ... Code from previous step

      let unsubscribe = try await realtime.off(topic: "chat.room1")
      print("Unsubscribed from chat.room1 => \\(unsubscribe)")

      try await realtime.close()
    }
}

var messageListener = ChatMessageListener()
try await realtime?.on(topic: "chat.room1", listener: messageListener!)

var sdkEventListenener = SDKEventListener()
try await realtime?.on(topic: "CONNECTED", listener: sdkEventListenener!)

client.connect()