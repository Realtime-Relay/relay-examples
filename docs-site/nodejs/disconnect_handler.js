import { DISCONNECTED } from "relayx-js"

client.on(DISCONNECTED, () => {
    console.log("Connection to Relay closed")
})