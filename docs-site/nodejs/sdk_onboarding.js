import { CONNECTED, Realtime } from "relayx-js"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

if(process.argv.length < 4){
    console.log("Usage: node <file>.js <type> <topic> <message>");
    console.log("type = pub or sub")
    process.exit();
}

var type = process.argv[2]
var topic = process.argv[3]
var message = process.argv[4]

console.log(`Type => ${type}`)
console.log(`Topic => ${topic}`)
console.log(`Message => ${message}`)
console.log()

client.connect()

await client.on(CONNECTED, async (status) => {
    console.log("Connected to relayX!")

    if(type == "pub"){
        console.log(`Sending message to topic => ${topic}`)
        console.log()
        var sent = await client.publish(topic, message);

        console.log(`Message sent => ${sent}`)
        console.log("Exiting script...")

        process.exit(0)
    }else if(type == "sub"){
        // Returns a boolean
        var subscribed = await client.on(topic, (data) => {
            console.log("We got a message!")
            console.log(data);
        })

        console.log(`Listening for messages on topic => ${topic}`)
    }else{
        console.log("Invalid $type value!")
        console.log("--------------------------------------")

        console.log("Usage: node <file>.js <type> <topic> <message>")
        console.log("type = pub or sub")
    }
})

setTimeout(async () => {
    await client.close()
    process.exit(0)
}, 15000)