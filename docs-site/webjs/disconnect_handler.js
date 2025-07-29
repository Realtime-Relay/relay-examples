import { DISCONNECTED } from "relayx-webjs"

client.on(DISCONNECTED, () => {
    console.log("Disconnect from Relay")
})