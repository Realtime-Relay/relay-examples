class ConnectionManager: MessageListener {
    func onMessage(_ message: Any) {
        println("Connected to Relay!")
    }
}

// Subscribe to system events
let connectionManager = ConnectionManager()
try await realtime.on(topic: SystemEvent.connected.rawValue, listener: connectionManager)