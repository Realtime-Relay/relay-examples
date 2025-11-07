class ConnectionManager: MessageListener {
    func onMessage(_ message: Any) {
        println(message)
    }
}

// Subscribe to system events
let connectionManager = ConnectionManager()
try await realtime.on(topic: SystemEvent.messageResend.rawValue, listener: connectionManager)