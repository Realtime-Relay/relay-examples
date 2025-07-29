import { Realtime } from "relayx-webjs"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()

// ... Application Code

client.connect()