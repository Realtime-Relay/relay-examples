class ConnectionManager: MessageListener {
    func onMessage(_ message: Any) {
        println(message)

        /*
        $message is an array of,
        [["topic": <String, topic which the message was sent to>, "message": <Your Message>, "resent": <Boolean, if it was resent or not>], ....]
        */
    }
}

// Subscribe to system events
let connectionManager = ConnectionManager()
try await realtime.on(topic: SystemEvent.messageResend.rawValue, listener: connectionManager)