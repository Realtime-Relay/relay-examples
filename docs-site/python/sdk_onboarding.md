## Install SDK
```
pip install relayx-py
```

## SDK Initalization
Initializing our SDKs with the API Key & Secret key so it can connect to the relayX Network.

```python
from relayx_py import Realtime

client = Realtime({
  "api_key": '$api_key',
  "secret": '$secret'
})

client.init()
```

## Publish A Message
We publish a message to `chat.room` when we connect to the relayX Network.

```python
sent = await client.publish("chat.room", "Hello world!")

print(f"Message sent => {sent}")
```

## Subscribe to a Topic
We initialize listeners for the topic `chat.room`

```python
def callback_fn(data):
    print("We got a message!")
    print(data)

# Returns a boolean
subscribed = await client.on("chat.room", callback_fn)
```

## Connect to the relayX Network
Connection is established by calling `connect()`

```python
await client.connect()
```

## Disconnect from the relayX Network
Connection is closed by calling `close()`

```python
await client.close()
```