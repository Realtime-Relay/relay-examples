# Swift SDK API Reference

### Constructor

#### `Realtime(apiKey: String, secret: String)`

Creates a new Realtime client instance.

**Parameters:**
- `apiKey` (String): Your Relay API key
- `secret` (String): Your Relay secret key

**Throws:**
- `RelayError.invalidCredentials` if credentials are invalid or missing

### Core Methods

#### `prepare(staging: Bool, opts: [String: Any])`

Prepares the Realtime client with configuration.

**Parameters:**
- `staging` (Bool): Use staging environment
- `opts` ([String: Any]): Configuration options
  - `debug` (Bool): Enable debug logging

**Throws:**
- `RelayError.invalidOptions` if options are invalid

#### `async connect()`

Establishes connection to the Relay Network.

**Returns:** `async throws -> Void`

**Throws:**
- `RelayError.notConnected` if connection fails
- `RelayError.invalidNamespace` if namespace retrieval fails

#### `async close()`

Closes the connection to Relay.

**Returns:** `async throws -> Void`

### Messaging Methods

#### `async on(topic: String, listener: MessageListener)`

Subscribes to messages on a topic.

**Parameters:**
- `topic` (String): Topic to subscribe to
- `listener` (MessageListener): Message listener interface
```swift
protocol MessageListener {
    func onMessage(_ message: [String: Any])
}
```

**Returns:** `async throws -> Bool` - Subscription success status

**Throws:**
- `TopicValidationError` if topic is invalid

#### `async off(topic: String)`

Unsubscribes from a topic.

**Parameters:**
- `topic` (String): Topic to unsubscribe from

**Returns:** `async throws -> Bool` - Unsubscribe success status

**Throws:**
- `TopicValidationError` if topic is invalid

#### `async publish(topic: String, message: Any)`

Publishes a message to a topic.

**Parameters:**
- `topic` (String): Topic name to publish to
- `message` (Any): Message payload. Must be one of:
  - String
  - Number 
  - JSON-serializable object

**Returns:** 
- `async throws -> Bool`: Success status of publish operation
  - `true` if message was published successfully
  - `false` if message was stored for offline delivery

**Throws:**
- `TopicValidationError` if topic is invalid
- `RelayError.invalidPayload` if message is invalid
- `RelayError.invalidTopic` if publishing to system topic

#### `async history(topic: String, start: Date, end: Date?, limit: Int?)`

Retrieves message history for a topic.

**Parameters:**
- `topic` (String): Topic to get history for
- `start` (Date): Start time for history query
- `end` (Date?, optional): End time for history query
- `limit` (Int?, optional): Maximum number of messages to retrieve

**Returns:** `async throws -> [[String: Any]]` where message format is:
```swift
[
    "id": String,
    "topic": String,
    "message": Any,
    "timestamp": String
]
```

**Throws:**
- `TopicValidationError` if topic is invalid
- `RelayError.invalidDate` if dates are invalid
- `RelayError.notConnected` if not connected

### Utility Methods

#### `isTopicValid(_ topic: String?) -> Bool`

Validates if a topic name meets all requirements.

**Parameters:**
- `topic` (String?): Topic name to validate

**Returns:** 
- `Bool`: Whether topic is valid
  - `true` if topic meets all requirements:
    - Non-nil and non-empty
    - Not a reserved system topic
    - Matches pattern: letters, numbers, underscores, hyphens, wildcards
    - No spaces
  - `false` otherwise

### Constants

Subscribe to these events using the `on()` method:

```swift
enum SystemEvent: String {
    case connected = "CONNECTED"
    case disconnected = "DISCONNECTED" 
    case reconnect = "RECONNECT"
    case reconnected = "RECONNECTED"
    case reconnecting = "RECONNECTING"
    case reconn_failed = "RECONN_FAILED"
    case messageResend = "MESSAGE_RESEND"
}
```

The events provide connection status and message delivery updates.