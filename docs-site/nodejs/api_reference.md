# Node.js SDK API Reference

## Constructor

### `new Realtime(config)`

Creates a new Realtime client instance.

**Parameters:**
- `config` (`Object`): Required configuration object
  - `api_key` (`string`): Your Relay API key
  - `secret` (`string`): Your Relay secret key

**Throws:**
- `Error` if config is invalid or missing required fields

## Methods

### `async init(staging?, opts?)`

Initializes the Realtime client.

**Parameters:**
- `staging` (`boolean`, optional): Use staging environment. Default: `false`
- `opts` (`Object`, optional): Additional options
  - `debug` (`boolean`): Enable debug logging

#### `async connect()`

Establishes connection to the Relay Network.

**Returns:** `Promise<void>`

### `async close()`

Closes the connection to Relay.

**Returns:** `Promise<void>`

### `async on(topic: string, callback: Function)`

Subscribes to messages on a topic.

**Parameters:**
- `topic` (`string`): Topic to subscribe to
- `callback` (`Function`): Callback function receiving messages
  ```typescript
  callback({
    id: string,
    topic: string, 
    data: any
  })
  ```

**Returns:** `Promise<boolean>` - Subscription success status

### `async off(topic: string)`

Unsubscribes from a topic.

**Parameters:**
- `topic` (`string`): Topic to unsubscribe from

**Returns:** `Promise<boolean>` - Unsubscribe success status

### `async publish(topic: string, data: any)`

Publishes a message to a topic.

**Parameters:**
- `topic` (`string`): Topic to publish to
- `data` (`any`): Message payload (must be JSON-serializable)

**Returns:** `Promise<boolean>` - Publish success status

### `async history(topic: string, start: Date, end?: Date)`

Retrieves message history for a topic.

**Parameters:**
- `topic` (`string`): Topic to get history for
- `start` (`Date`): Start time 
- `end` (`Date`, optional): End time

**Returns:** `Promise<Array<Message>>` where Message is:
```typescript
{
  id: string,
  topic: string,
  message: any,
  timestamp: string
}
```

## Utility Methods

### `isTopicValid(topic: string)`

Validates if a topic name is valid.

**Parameters:**
- `topic` (`string`): Topic name to validate

**Returns:** `boolean`

### `isMessageValid(message: any)` 

Validates if a message can be published.

**Parameters:**
- `message` (`any`): Message to validate

**Returns:** `boolean`

## Events

Subscribe to these events using the `on()` method:

- `CONNECTED`: Connection established
- `DISCONNECTED`: Connection lost
- `RECONNECT`: Reconnection status changes
  - Callback receives: `"RECONNECTING"` or `"RECONNECTED"`
- `MESSAGE_RESEND`: Offline messages resent
  - Callback receives: Array of message statuses

## Constants

```javascript
CONNECTED = "CONNECTED"
DISCONNECTED = "DISCONNECTED" 
RECONNECT = "RECONNECT"
MESSAGE_RESEND = "MESSAGE_RESEND"
SERVER_DISCONNECT = "SERVER_DISCONNECT"
```