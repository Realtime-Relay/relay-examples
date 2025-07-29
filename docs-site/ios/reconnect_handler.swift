class ConnectionManager: MessageListener {
    func onMessage(_ message: Any) {
        if let event = message as? String {
            switch event {
            case "RECONNECTING":
                println("Looks like we're not connected, attempting to reconnect to Relay...")
            case "RECONNECTED":
                println("Reconnected to Relay! :D")
            case "RECONN_FAIL":
                println("Failed to reconnect to Relay :(")
            default:
                break
            }
        }
    }
}

// Subscribe to system events
let connectionManager = ConnectionManager()
try await realtime.on(topic: SystemEvent.reconnect.rawValue, listener: connectionManager)