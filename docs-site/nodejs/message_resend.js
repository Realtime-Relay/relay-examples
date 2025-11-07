import { MESSAGE_RESEND } from "relayx-js"

client.on(MESSAGE_RESEND, (data) => {
    console.log(data)
})