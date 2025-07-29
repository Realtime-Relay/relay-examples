import com.realtime.relay.realtimeSDK.Realtime

client.on(Realtime.RECONNECT) { status ->
    if(status == Realtime.RECONNECTING){
        Log.d("Relay", "Looks like we're not connected, attempting to reconnect to Relay...")
    }else if(status == Realtime.RECONNECTED){
        Log.d("Relay", "Reconnected to Relay! :D")
    }else if(status == Realtime.RECONN_FAIL){
        Log.d("Relay", "Failed to reconnect to Relay :(")
    }
}