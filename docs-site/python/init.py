from relayx_py import Realtime

client = Realtime({
  "api_key": '${apiKeys.api_key}',
  "secret": '${apiKeys.secret}'
})

client.init()