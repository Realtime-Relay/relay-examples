# Relay Python SDK API Reference

### Constructor

#### `Realtime(config)`

Creates a new Realtime instance.

Parameters:
- `config` (dict): Configuration object containing:
  - `api_key` (str): Your Relay API key
  - `secret` (str): Your Relay API secret

### Core Methods

#### `init(staging=False, opts=None)`

Initializes the SDK with configuration options.

Parameters:
- `staging` (bool): Whether to use staging environment
- `opts` (dict): Additional options
  - `debug` (bool): Enable debug logging

#### `async connect()`

Establishes connection to the Relay Network.

#### `async close()`

Closes the connection to Relay.

### Messaging Methods

#### `async publish(topic, data)`

Publishes a message to a topic.

Parameters:
- `topic` (str): The topic to publish to
- `data` (str|number|dict): The message payload

Returns:
- `bool`: True if successful

#### `async on(topic, func)`

Subscribes to a topic with a callback function.

Parameters:
- `topic` (str): Topic to subscribe to 
- `func` (callable): Callback function

Returns:
- `bool`: True if successful

#### `async off(topic)`

Unsubscribes from a topic.

Parameters:
- `topic` (str): Topic to unsubscribe from

Returns:
- `bool`: True if successful

#### `async history(topic, start, end=None)`

Gets message history for a topic.

Parameters:
- `topic` (str): Topic to get history for
- `start` (datetime): Start time
- `end` (datetime, optional): End time

Returns:
- `list`: List of historical messages

### Utility Methods

#### `is_topic_valid(topic)`

Validates if a topic string is valid.

Parameters:
- `topic` (str): Topic to validate

Returns:
- `bool`: True if valid

### Events

Subscribe to these events using the `on()` method:

- `CONNECTED`: Connection established
- `DISCONNECTED`: Connection closed
- `RECONNECT`: Connection reconnecting/reconnected
- `MESSAGE_RESEND`: Offline messages resent