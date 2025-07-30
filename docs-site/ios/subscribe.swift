// Create a message listener
class MyMessageListener: MessageListener {
    func onMessage(_ message: Any) {
        print("Received message: \(message)")
    }
}

let listener = MyMessageListener()

// Returns a boolean
let subscribed =  try await client.on(topic: "chat.room1", listener: listener)

// -------------------------------------------------
// $message is a dict
[
    "id": "<MESSAGE ID>",
    "topic": "<TOPIC MATCHING TOPIC / WILDCARD TOPIC>",
    "data": <Actual message as string, number or json>
]