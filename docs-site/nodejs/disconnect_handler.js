import { DISCONNECTED } from "relayx-js"

client.on(DISCONNECTED, () => {
    console.log("Disconnect from Relay")
})