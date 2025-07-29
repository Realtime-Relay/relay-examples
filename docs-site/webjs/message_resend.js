import { MESSAGE_RESEND } from "relayx-webjs"

client.on(MESSAGE_RESEND, (data) => {
    console.log(data)

    /**
     * $data is an array of,
     * [{"topic": <String, topic which the message was sent to>, "message": <Your Message>, "resent": <Boolean, if it was resent or not>}, ....]
     */
})