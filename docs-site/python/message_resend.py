from relayx_py import Realtime

def callback_fn(data):
    print(data)

await client.on(Realtime.MESSAGE_RESEND, callback_fn)