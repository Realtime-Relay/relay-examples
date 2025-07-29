class ConnectionManager: MessageListener {
    func onMessage(_ message: Any) {
        println("Connection to Relay closed")
    }
}

// Subscribe to system events
let connectionManager = ConnectionManager()
try await realtime.on(topic: SystemEvent.disconnected.rawValue, listener: connectionManager)