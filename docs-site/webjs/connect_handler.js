import { CONNECTED } from "relayx-webjs"

client.on(CONNECTED, () => {
    console.log("Connected to Relay!")
})