import { DISCONNECTED } from "relayx-webjs"

client.on(DISCONNECTED, () => {
    console.log("Connection to Relay closed")
})