## Install SDK
1. Add this to your settings.gradle file (library is hosted on JitPack):

    ```gradle
    repositories {
        google()
        mavenCentral()
        maven { url = uri("https://jitpack.io") }
    }
    ```
2. Add this to your app build.gradle file:

    ```gradle
    implementation("com.github.Realtime-Relay:relayx-android:1.0.3")
    ```

## SDK Initalization
Initializing our SDKs with the API Key & Secret key so it can connect to the relayX Network.

```kotlin
import com.realtime.relay.realtimeSDK.Realtime

val client = Realtime(this, 
                      "$api_key",
                      "$secret")
                      
client.init(staging = false, opts = mapOf("debug" to false))
```

## Publish A Message
We publish a message to `chat.room` when we connect to the relayX Network.

```kotlin
val sent = client.publish("chat.room", "Hello world!")

Log.d("Message_Send_Status", sent)
```

## Subscribe to a Topic
We initialize listeners for the topic `chat.room`

```kotlin
// Returns a boolean
let subscribe = client.on("chat.room") { payload -> 
  Log.d("Message", payload)
}
```

## Connect to the relayX Network
Connection is established by calling `connect()`

```kotlin
client.connect()
```

## Disconnect from the relayX Network
Connection is closed by calling `close()`

```kotlin
client.close()
```