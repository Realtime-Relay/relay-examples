
/*
* publish() returns a boolean
* Returns true if message was published
* Returns false if message was not published
*/

let success = try await realtime?.publish(topic: topic, message: [
    "user_name": "John Doe",
    "message": "How's it going fam?"
])

print("Message sent => \\(success)")