import { RECONNECT } from "relayx-webjs"

client.on(RECONNECT, (status) => {
    
    if(status == "RECONNECTING"){
        console.log("Looks like we're not connected, attempting to reconnect to Relay...")
    }else if(status == "RECONNECTED"){
        console.log("Reconnected to Relay! :D")
    }else if(status == "RECONN_FAIL"){
        console.log("Failed to reconnect to Relay :(")
    }

})