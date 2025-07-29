import com.realtime.relay.realtimeSDK.Realtime

client.on(Realtime.DISCONNECTED) { 
    Log.d("Relay", "Connection to Relay closed")
}