/**
 * publish() returns a boolean
 * Returns true if message was published
 * Returns false if message was not published
 */
var sent = await client.publish("chat.room1", {
    user_name: "John Doe",
    message: "How's it going fam?"
});

console.log("Message sent => " + sent); 