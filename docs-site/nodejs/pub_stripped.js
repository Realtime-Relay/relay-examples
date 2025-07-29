var sent = await client.publish("<YOUR TOPIC>", {
    user_name: "John Doe",
    message: "How's it going fam?"
});

var sent = await client.publish("<YOUR TOPIC>", "String messages are valid!");

// So are numbers
var sent = await client.publish("<YOUR TOPIC>", 1234);

var sent = await client.publish("<YOUR TOPIC>", 1234.231);