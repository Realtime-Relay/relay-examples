val message = buildMap<String, Any> {
    put("user_name", "John Doe")
    put("message", "How's it going fam?")
}

/* 
* publish() returns a boolean
* Returns true if message was published
* Returns false if message was not published
*/
val sent = client.publish("chat.room1", message)

Log.d("Message", "Message sent => $sent")