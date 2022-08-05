import zmq
import time

if __name__ == '__main__':
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