1. Clone the [Android Repo](https://github.com/Realtime-Relay/relayx-android/tree/main)
2. Open the repo in Android Studio
3. Copy your API Key & Secret from Step 2.
4. Sync Gradle
5. Run on **another** emulator or device
6. Enter your `chat.room` in the topic field and tap **Connect**
7. When “Disconnected” becomes “Connected”, you’re ready to send and receive messages.
8. Send a message from the first device & hit send.
9. The same message should be received on device 1.

relayX code here => [RealtimeService.kt](https://github.com/Realtime-Relay/relayx-android/blob/main/app/src/main/java/com/relay/realtime/exampleapp/RealtimeService.kt)