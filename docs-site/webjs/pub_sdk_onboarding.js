var sent = await client.publish("chat.room", "Hello world!");

console.log(`Message sent => ${sent}`)