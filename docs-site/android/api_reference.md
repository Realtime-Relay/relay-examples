# Android Kotlin SDK API Reference

### Constructor

#### `Realtime(context, apiKey, secretKey, callbackDispatcher)`

Creates a new Realtime client instance.

**Parameters:**
- `context` (Context): Android application context
- `apiKey` (String): Your Relay API key
- `secretKey` (String): Your Relay secret key
- `callbackDispatcher` (CoroutineDispatcher, optional): Dispatcher for callbacks. Default: `Dispatchers.Main.immediate`

**Throws:**
- `IllegalArgumentException` if apiKey or secretKey is empty/blank

### Core Methods

#### `init(staging: Boolean, opts: Map<String, Any>?)`

Initializes the Realtime client.

**Parameters:**
- `staging` (Boolean): Use staging environment
- `opts` (Map<String, Any>?): Additional options
  - `debug` (Boolean): Enable debug logging

**Throws:**
- `IllegalArgumentException` if opts is null

#### `suspend fun connect()`

Establishes connection to the Relay Network.

**Returns:** `Unit`

#### `suspend fun close()`

Closes the connection to Relay.

**Returns:** `Unit`

### Messaging Methods

#### `suspend fun on(topic: String, listener: (JsonObject) -> Unit)`

Subscribes to messages on a topic.

**Parameters:**
- `topic` (String): Topic to subscribe to
- `listener` (Function): Callback function receiving messages
  ```kotlin
  listener({
    id: String,
    topic: String, 
    data: JsonObject
  })
  ```

**Returns:** `Boolean` - Subscription success status

**Throws:**
- `IllegalArgumentException` if topic is invalid

#### `fun off(topic: String)`

Unsubscribes from a topic.

**Parameters:**
- `topic` (String): Topic to unsubscribe from

**Returns:** `Boolean` - Unsubscribe success status

**Throws:**
- `IllegalArgumentException` if topic is invalid

#### `suspend fun publish(topic: String, message: Any)`

Publishes a message to a topic.

**Parameters:**
- `topic` (String): Topic name to publish to
- `message` (Any): Message payload. Must be:
  - String
  - Number
  - Map

**Returns:** `Boolean` - Success status of publish operation

**Throws:**
- `IllegalArgumentException` if topic is invalid
- `IllegalArgumentException` if message is invalid type

#### `suspend fun history(topic: String, start: Long, end: Long?)`

Retrieves message history for a topic.

**Parameters:**
- `topic` (String): Topic to get history for
- `start` (Long): Start timestamp in milliseconds
- `end` (Long?, optional): End timestamp in milliseconds

**Returns:** `List<Any>` - List of messages

**Throws:**
- `IllegalArgumentException` if topic is invalid
- `IllegalArgumentException` if start is null
- `IllegalArgumentException` if end <= start

### Utility Methods

#### `fun isTopicValid(topic: String)`

Validates if a topic name is valid.

**Parameters:**
- `topic` (String): Topic name to validate

**Returns:** `Boolean`

#### `fun isMessageValid(msg: Any)`

Validates if a message can be published.

**Parameters:**
- `msg` (Any): Message to validate

**Throws:**
- `IllegalArgumentException` if message type is invalid

### Events

Subscribe to these events using the `on()` method:

- `CONNECTED`: Connection established
- `DISCONNECTED`: Connection lost
- `RECONNECT`: Connection status changes
  - Callback receives: `"RECONNECTING"` or `"RECONNECTED"`
- `MESSAGE_RESEND`: Offline messages resent
- `RECONN_FAIL`: Reconnection failed

### Constants

```kotlin
companion object {
    val CONNECTED = "CONNECTED"
    val RECONNECT = "RECONNECT"
    val MESSAGE_RESEND = "MESSAGE_RESEND" 
    val DISCONNECTED = "DISCONNECTED"
    val RECONNECTING = "RECONNECTING"
    val RECONNECTED = "RECONNECTED"
    val RECONN_FAIL = "RECONN_FAIL"
}
```