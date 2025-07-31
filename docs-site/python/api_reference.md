# Python SDK API Reference

### Constructor

#### `Realtime(config)`

Creates a new Realtime client instance.

**Parameters:**
- `config` (dict): Required configuration object
  - `api_key` (str): Your Relay API key
  - `secret` (str): Your Relay secret key

**Throws:**
- `ValueError` if config is invalid or missing required fields

### Core Methods

#### `async init(staging=False, opts=None)`

Initializes the Realtime client.

**Parameters:**
- `staging` (bool, optional): Use staging environment. Default: `False`
- `opts` (dict, optional): Additional options
  - `debug` (bool): Enable debug logging

**Returns:** `None`

#### `async connect()`

Establishes connection to the Relay Network.

**Returns:** `None`

#### `async close()`

Closes the connection to Relay.

**Returns:** `None`

### Messaging Methods

#### `async on(topic: str, callback: Callable)`

Subscribes to messages on a topic.

**Parameters:**
- `topic` (str): Topic to subscribe to
- `callback` (Callable): Callback function receiving messages
  ```python
  def callback(message: dict):
      """
      message = {
          "id": str,
          "topic": str,
          "data": Any
      }
      """
      pass
  ```

**Returns:** `bool` - Subscription success status

**Throws:**
- `ValueError` if topic is None/empty
- `ValueError` if topic format is invalid
- `ValueError` if callback is not callable

#### `async off(topic: str)`

Unsubscribes from a topic.

**Parameters:**
- `topic` (str): Topic to unsubscribe from

**Returns:** `bool` - Unsubscribe success status

**Throws:**
- `ValueError` if topic is None/empty
- `ValueError` if topic format is invalid

#### `async publish(topic: str, data: Union[str, int, float, dict])`

Publishes a message to a topic.

**Parameters:**
- `topic` (str): Topic name to publish to
- `data`: Message payload. Must be one of:
  - str
  - int/float
  - dict (JSON-serializable)

**Returns:** 
- `bool`: Success status of publish operation
  - `True` if message was published successfully
  - `False` if message was added to offline buffer

**Throws:**
- `ValueError` if topic is None/empty
- `ValueError` if topic format is invalid
- `ValueError` if message is None
- `ValueError` if message type is invalid

#### `async history(topic: str, start: datetime, end: Optional[datetime] = None)`

Retrieves message history for a topic.

**Parameters:**
- `topic` (str): Topic to get history for
- `start` (datetime): Start time for history query
- `end` (datetime, optional): End time for history query

**Returns:** `List[Dict]` where each dict contains:
```python
{
    "id": str,
    "topic": str,
    "message": Any,
    "timestamp": str
}
```

**Throws:**
- `ValueError` if topic is invalid
- `ValueError` if start datetime is missing/invalid
- `ValueError` if end datetime is invalid
- `ValueError` if start datetime is after end datetime

### Utility Methods

#### `is_topic_valid(topic: str)`

Validates if a topic name is valid.

**Parameters:**
- `topic` (str): Topic name to validate

**Returns:** `bool`

#### `is_message_valid(message: Any)`

Validates if a message can be published.

**Parameters:**
- `message` (Any): Message to validate

**Returns:**
- `bool`: Whether message is valid
  - `True` if message is str, number, or JSON-serializable
  - `False` otherwise

**Throws:**
- `ValueError` if message is None

### Events

Subscribe to these events using the `on()` method:

- `CONNECTED`: Connection established
- `DISCONNECTED`: Connection closed
- `RECONNECT`: Reconnection status changes
  - Callback receives: `"RECONNECTING"`, `"RECONN_FAIL"` or `"RECONNECTED"`
- `MESSAGE_RESEND`: Offline messages resent
  - Callback receives: List of message statuses

### Constants

```python
CONNECTED = "CONNECTED"
DISCONNECTED = "DISCONNECTED"
RECONNECT = "RECONNECT" 
MESSAGE_RESEND = "MESSAGE_RESEND"
```