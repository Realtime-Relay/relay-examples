from relayx_py import Realtime

client = Realtime({
  "api_key": '$api_key',
  "secret": '$secret'
})

client.init()

# ... Application Code

await client.connect()