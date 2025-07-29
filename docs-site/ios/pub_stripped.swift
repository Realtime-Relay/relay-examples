let success = try await realtime?.publish(topic: "<YOUR TOPIC>", message: [
    "user_name": "John Doe",
    "message": "How's it going fam?"
])

let success = try await realtime?.publish(topic: "<YOUR TOPIC>", message: "String messages are valid!")

// So are numbers
let success = try await realtime?.publish(topic: "<YOUR TOPIC>", message: 1234)

let success = try await realtime?.publish(topic: "<YOUR TOPIC>", message: 1234.123)