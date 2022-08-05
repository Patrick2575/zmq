# Client - Server 'Hello, World'

In this example we use the most basic pattern, `client/server`, where client sends a request and server replies to the request

We’ll make a `client` and a `server`. The client sends "Hello" to the server, which replies with "World"

## Server

```python
  port = 5555
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind(f'tcp://*:{port}')
  print(f'Server listening on tcp:{port} ...')
  while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f'Received request: {message.decode("utf-8")}')
    time.sleep (1)  
    #socket.send_string('World')
    socket.send(bytes('World', 'utf-8'))
```

After executing this code above, the server will be up und running waiting for clients to connect (`socket.recv()` blocks until someone sends a request).

You could throw thousands of clients at this server, all at once, and it would continue to work happily
and quickly.

## Client

```python
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect (f'tcp://localhost:5555') # connect to the server at 5555 port
                                           # Note: same socket can connect to two different servers

  # now connection is done, lets send some requests
  for i in range(100):
    print('Sending request `Hello` ...')
    #socket.send_string('Hello')
    socket.send(bytes('Hello', 'utf-8'))
    # get the reply
    res = message = socket.recv() # this will block until someone responds
    print(f'Received reply : {res.decode("utf-8")}')
```

After executing this code above, the client will connect to the server and send 10 requests.

Requests are sent one by one, and for each request, the client waits for a reply (`socket.recv()` blocks until someone sends a response)

## Notes

* For fun, try starting the client and then starting the server, see how it all still works, then
think for a second what this means

* If you kill the server (`Ctrl-C`) and restart it, the client won’t recover properly.
Recovering from crashing processes isn’t quite that easy. Making a `reliable request-reply` flow is complex enough that it will be subject of its own chapter

* You may have noticed that when we call `socket.send` to send a string, we needed to convert the string into bytes. This is because `PyZMQ` is a wrapper for a C library and uses bytes. But since `Python 3`, a `str` is a full unicode object and a unicode objects have a wide range of presentation. They are not stored as bytes according to their encoding, but rather in a format called UCS. On some platforms (macOS, Windows), the storage is UCS-2, which is 2 bytes per character. On most *ix systems, it is UCS-4, or 4 bytes per character. This makes unicode objects to be `platform dependent` and as result, `str` objects in Python 3 don’t even provide the buffer interface. You simply cannot get the raw bytes of a unicode object without specifying the encoding for the bytes. This is why we have used bytes instead of `str` objects. Each time `PyZMQ` requires bytes (`socket.send/recv, socket.get/setsockopt, socket.bind/connect`) and receives a unicode object it raises an exception. Still, as users will quite frequently have unicode strings that they want to send `PyZMQ` provides `socket.<method>_string()` wrappers. These methods simply wrap their bytes counterpart by encoding/decoding to/from bytes and they take an `encoding` argument that defaults to utf-8.
