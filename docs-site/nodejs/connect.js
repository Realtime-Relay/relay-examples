import { Realtime } from "relayx-js"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

// ... Application Code

client.connect()