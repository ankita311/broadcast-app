# Minimal Publisher/Subscriber Service

A simple, in-memory publisher/subscriber service built with Python's built-in libraries.

## Features

- ✅ **Topic-based messaging**: Subscribe to specific topics
- ✅ **Multiple subscribers**: Multiple callbacks per topic
- ✅ **Asynchronous processing**: Background worker thread
- ✅ **Thread-safe**: Uses Python's Queue for thread safety
- ✅ **Simple API**: Easy to use publish/subscribe methods
- ✅ **No external dependencies**: Uses only Python standard library

## Quick Start

### Run the example:
```bash
python pubsub_service.py
```

### Run the test:
```bash
python test_pubsub.py
```

## Basic Usage

```python
from pubsub_service import PubSubService

# Create and start the service
pubsub = PubSubService()
pubsub.start()

# Define a subscriber callback
def my_subscriber(message):
    print(f"Received: {message.data}")

# Subscribe to a topic
pubsub.subscribe("my_topic", my_subscriber)

# Publish a message
pubsub.publish("my_topic", "Hello, World!")

# Stop the service
pubsub.stop()
```

## Architecture

- **Message Queue**: Uses `queue.Queue` for thread-safe message handling
- **Worker Thread**: Background thread processes messages asynchronously
- **Topic Registry**: Dictionary mapping topics to subscriber callbacks
- **Message Structure**: Simple dataclass with topic, data, and timestamp

## Next Steps (Incremental Improvements)

1. **Persistence**: Add message persistence to files/database
2. **Network Support**: Add TCP/HTTP endpoints
3. **Message Filtering**: Add wildcard topic matching
4. **Message Acknowledgment**: Add delivery confirmation
5. **Load Balancing**: Support multiple worker threads
6. **Monitoring**: Add metrics and health checks

## Current Limitations

- In-memory only (messages lost on restart)
- Single-threaded message processing
- No message persistence
- No network capabilities
- No authentication/authorization 