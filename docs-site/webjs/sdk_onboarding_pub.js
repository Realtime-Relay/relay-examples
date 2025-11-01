import { CONNECTED, Realtime } from "relayx-webjs"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

if(process.argv.length < 4){
    console.log("Usage: node <file>.js <topic> <message>");
    console.log("type = pub or sub")
    process.exit();
}

var topic = process.argv[2]
var message = process.argv[3]

client.connect()

await client.on(CONNECTED, async (status) => {
    console.log("Connected to relayX!")

    console.log(`Sending message to topic => ${topic}`)
    console.log()

    var sent = await client.publish(topic, message);

    console.log(`Message sent => ${sent}`)
    console.log("Exiting script...")

    process.exit(0)
})

 setTimeout(async () => {
    await client.close()
    process.exit(0)
}, 15000)