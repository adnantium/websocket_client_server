# Websocket Client &amp; Server
A very simple example using python's `asyncio` and `websockets` library.

* Multiple clients can connect to a server listening on port 6789.
* The server keeps a list of connected clients and keeps sending a random number to each one.

## Running it

Open 3 terminal windows and run:
1. `$ python websocket_server.py`
2. `$ python websocket_client.py`
3. `$ python websocket_client.py`

### 1. Server
```
$ python websocket_server.py 
Started socket server: <websockets.server.Serve object at 0x10e0b23a0> ...
New connection from: ('::1', 50966, 0, 0) (1 total)
Got: [Please send me a number...] from socket [4530578672]
Sending [53] to socket [4530578672]
Sending [32] to socket [4530578672]
New connection from: ('::1', 50968, 0, 0) (2 total)
Got: [Please send me a number...] from socket [4530579008]
Sending [50] to socket [4530579008]
Sending [50] to socket [4530578672]
Sending [43] to socket [4530579008]
Sending [43] to socket [4530578672]
Disconnected from socket [4530578672]...
Sending [49] to socket [4530579008]
Disconnected from socket [4530579008]...
```

### Client #1
```
$ python websocket_client.py 
Sending [Please send me a number...] to connection [4539402704]
Got: 50
Got: 43
Got: 49
^CEnding...

```

### Client #2
```
$ python websocket_client.py 
Sending [Please send me a number...] to connection [4342327712]
Got: 53
Got: 32
Got: 50
Got: 43
^CEnding...
```

## TODO:
* Need some graceful exception handling and a shutdown and cleanup process.
