## Install SDK
```
npm i relayx-webjs
```

This is just an explanation. Skip to step 4 to get a full code example.

## SDK Initalization
Initializing our SDKs with the API Key & Secret key so it can connect to the relayX Network.

```js
import { Realtime } from "relayx-webjs"

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

client.init()
```

## Publish A Message
We publish a message to `chat.room` when we connect to the relayX Network.

```js
var sent = await client.publish("chat.room", "Hello world!");

console.log(`Message sent => ${sent}`)
```

## Subscribe to a Topic
We initialize listeners for the topic `chat.room`

```js
var subscribed = await client.on("chat.room", (data) => {
    console.log("We got a message!")
    console.log(data);
})
```

## Connect to the relayX Network
Connection is established by calling `connect()`

```js
await client.connect()
```

## Disconnect from the relayX Network
Connection is closed by calling `close()`

```js
await client.close()
```
