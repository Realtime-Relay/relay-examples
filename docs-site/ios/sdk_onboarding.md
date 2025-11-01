## Install SDK
1. In XCode, go to File > Add Package Dependencies...
2. In the search bar, paste: github.com/Realtime-Relay/relayx-ios.git
3. Select the latest version & then hit "Add Package"

## SDK Initalization
Initializing our SDKs with the API Key & Secret key so it can connect to the relayX Network.

```swift
import Realtime

var client = Realtime(
    apiKey: "$api_key",
    secret: "$secret"
)

client?.prepare(staging: false, opts: ["debug": false])
```

## Publish A Message
We publish a message to `chat.room` when we connect to the relayX Network.

```swift
let success = try await realtime?.publish(topic: "chat.room", message: "Hello world!")

print("Message sent: \(success)")
```

## Subscribe to a Topic
We initialize listeners for the topic `chat.room`

```swift
// Create a message listener
class MyMessageListener: MessageListener {
    func onMessage(_ message: Any) {
        print("Received message: \(message)")
    }
}

let listener = MyMessageListener()

// Returns a boolean
let subscribed =  try await client.on(topic: "chat.room", listener: listener)
```

## Connect to the relayX Network
Connection is established by calling `connect()`

```swift
client.connect()
```

## Disconnect from the relayX Network
Connection is closed by calling `close()`

```swift
client.close()
```