import Realtime

var client = Realtime(
    apiKey: "$api_key",
    secret: "$secret"
)

client?.prepare(staging: false, opts: ["debug": false])

// ... Application Code

client?.close()

// ... Application Code

client?.connect()