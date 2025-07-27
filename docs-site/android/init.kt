import com.realtime.relay.realtimeSDK.Realtime

val client = Realtime(this, 
                      "${apiKeys.api_key}",
                      "${apiKeys.secret}")
                      
client.init(staging = false, opts = mapOf("debug" to false))