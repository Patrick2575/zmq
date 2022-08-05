import zmq

if __name__ == '__main__':
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