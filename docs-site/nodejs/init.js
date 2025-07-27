import { Realtime, CONNECTED } from "relayx-js"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()