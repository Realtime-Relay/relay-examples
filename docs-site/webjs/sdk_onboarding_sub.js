import { CONNECTED, Realtime } from "relayx-webjs"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

if(process.argv.length < 3){
    console.log("Usage: node <file>.js <topic>");
    console.log("type = pub or sub")
    process.exit();
}

var topic = process.argv[2]

client.connect()

await client.on(CONNECTED, async (status) => {
    console.log("Connected to relayX!")

    console.log(`Listening for messages on topic => ${topic}`)
    console.log()

    await client.on(topic, (data) => {
        console.log("We got a message!")
        console.log(data)

        console.log()
        console.log("Exiting script...")

        process.exit(0)
    });
})

 setTimeout(async () => {
    await client.close()
    process.exit(0)
}, 15000)