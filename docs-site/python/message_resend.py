from relayx_py import Realtime

def callback_fn(data):
    print(data)

    # $data is an array of,
    # [{"topic": <String, topic which the message was sent to>, "message": <Your Message>, "resent": <Boolean, if it was resent or not>}, ....]

await client.on(Realtime.MESSAGE_RESEND, callback_fn)