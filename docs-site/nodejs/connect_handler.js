import { CONNECTED } from "relayx-js"

client.on(CONNECTED, () => {
    console.log("Connected to Relay!")
})