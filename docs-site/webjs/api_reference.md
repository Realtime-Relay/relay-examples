# WebJS SDK API Reference

### Constructor

#### `new Realtime(config)`

Creates a new Realtime client instance.

**Parameters:**
- `config` (Object): Required configuration object
  - `api_key` (string): Your Relay API key
  - `secret` (string): Your Relay secret key

**Throws:**
- `Error` if config is invalid or missing required fields

### Core Methods

#### `async init(staging?, opts?)`

Initializes the Realtime client.

**Parameters:**
- `staging` (boolean, optional): Use staging environment. Default: `false`
- `opts` (Object, optional): Additional options
  - `debug` (boolean): Enable debug logging

**Returns:** `Promise<void>`

#### `async connect()`

Establishes connection to the Relay Network.

**Returns:** `Promise<void>`

#### `async close()`

Closes the connection to Relay.

**Returns:** `Promise<void>`

### Messaging Methods

#### `async on(topic: string, callback: Function)`

Subscribes to messages on a topic.

**Parameters:**
- `topic` (string): Topic to subscribe to
- `callback` (Function): Callback function receiving messages
  ```typescript
  callback({
    id: string,
    topic: string, 
    data: any
  })
  ```

**Returns:** `Promise<boolean>` - Subscription success status

**Throws:**
- `Error` if topic is null/undefined/empty
- `Error` if topic format is invalid
- `Error` if callback is not a function

#### `async off(topic: string)`

Unsubscribes from a topic.

**Parameters:**
- `topic` (string): Topic to unsubscribe from

**Returns:** `Promise<boolean>` - Unsubscribe success status

**Throws:**
- `Error` if topic is null/undefined/empty 
- `Error` if topic format is invalid

#### `async publish(topic: string, data: string | number | object)`

Publishes a message to a topic.

**Parameters:**
- `topic` (string): Topic name to publish to
- `data`: Message payload. Must be one of:
  - String
  - Number 
  - JSON-serializable object

**Returns:** 
- `Promise<boolean>`: Success status of publish operation
  - `true` if message was published successfully
  - `false` if message was added to offline buffer

**Throws:**
- `Error` if topic is null/undefined/empty
- `Error` if topic format is invalid
- `Error` if message is null/undefined
- `Error` if message type is not string/number/JSON

#### `async history(topic: string, start: Date, end?: Date)`

Retrieves message history for a topic.

**Parameters:**
- `topic` (string): Topic to get history for
- `start` (Date): Start time for history query
- `end` (Date, optional): End time for history query

**Returns:** `Promise<Array<Message>>` where Message is:
```typescript
{
  id: string,
  topic: string,
  message: any,
  timestamp: string
}
```

**Throws:**
- `Error` if topic is invalid
- `Error` if start date is missing/invalid
- `Error` if end date is invalid
- `Error` if start date is after end date

### Utility Methods

#### `isTopicValid(topic: string)`

Validates if a topic name is valid.

**Parameters:**
- `topic` (string): Topic name to validate

**Returns:** boolean

#### `isMessageValid(message: any)`

Validates if a message can be published.

**Parameters:**
- `message` (any): Message to validate

**Returns:**
- `boolean`: Whether message is valid
  - `true` if message is string, number, or JSON-serializable
  - `false` otherwise

**Throws:**
- `Error` if message is null/undefined

### Events

Subscribe to these events using the `on()` method:

- `CONNECTED`: Connection established
- `DISCONNECTED`: Connection lost
- `RECONNECT`: Reconnection status changes
  - Callback receives: `"RECONNECTING"`, `"RECONN_FAIL"` or `"RECONNECTED"`
- `MESSAGE_RESEND`: Offline messages resent
  - Callback receives: Array of message statuses

### Constants

```javascript
CONNECTED = "CONNECTED"
DISCONNECTED = "DISCONNECTED"
RECONNECT = "RECONNECT" 
MESSAGE_RESEND = "MESSAGE_RESEND"
SERVER_DISCONNECT = "SERVER_DISCONNECT"
```