import com.realtime.relay.realtimeSDK.Realtime

val client = Realtime(this, 
                      "$api_key",
                      "$secret")
                      
client.init(staging = false, opts = mapOf("debug" to false))