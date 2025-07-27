import Realtime

var client = Realtime(
    apiKey: "${apiKeys.api_key}",
    secret: "${apiKeys.secret}"
)

client?.prepare(staging: false, opts: ["debug": false])