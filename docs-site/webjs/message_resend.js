import { MESSAGE_RESEND } from "relayx-webjs"

client.on(MESSAGE_RESEND, (data) => {
    console.log(data)
})