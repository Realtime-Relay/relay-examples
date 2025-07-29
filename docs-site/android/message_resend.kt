import com.realtime.relay.realtimeSDK.Realtime

client.on(Realtime.MESSAGE_RESEND) { payload -> 
    Log.d("Message", payload)

    /*
    $payload is an array of,
    [{"topic": <String, topic which the message was sent to>, "message": <Your Message>, "resent": <Boolean, if it was resent or not>}, ....]
    */
}