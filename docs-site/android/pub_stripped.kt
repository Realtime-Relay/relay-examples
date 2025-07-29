val message = buildMap<String, Any> {
    put("user_name", "John Doe")
    put("message", "How's it going fam?")
}

val sent = client.publish("<YOUR TOPIC>", message)

val sent = client.publish("<YOUR TOPIC>", "String messages are valid!")

// So are numbers
val sent = client.publish("<YOUR TOPIC>", 1234)

val sent = client.publish("<YOUR TOPIC>", 1234.24)
