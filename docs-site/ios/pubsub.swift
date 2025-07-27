private class ChatMessageListener: MessageListener {
        
    func onMessage(_ data: Any) {
      print("We got a message!")
      print(data)
    }
}

private class SDKEventListener: MessageListener {
        
    func onMessage(_ data: Any) {
      print("Connected to Relay!")
      
      let success = try await realtime?.publish(topic: topic, message: [
          "user_name": "John Doe",
          "message": "How's it going fam?"
      ])

      print("Message sent => \\(success)")
    }
}

var messageListener = ChatMessageListener()
try await realtime?.on(topic: "chat.room1", listener: messageListener!)

var sdkEventListenener = SDKEventListener()
try await realtime?.on(topic: "CONNECTED", listener: sdkEventListenener!)

client.connect()