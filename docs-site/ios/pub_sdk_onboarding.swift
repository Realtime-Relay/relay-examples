let success = try await realtime?.publish(topic: "chat.room", message: "Hello world!")

print("Message sent: \(success)")