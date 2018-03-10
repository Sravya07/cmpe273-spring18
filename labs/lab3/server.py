import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
repsock = context.socket(zmq.PULL)
repsock.bind("tcp://127.0.0.1:5555")
pubsock=context.socket(zmq.PUB)
pubsock.bind("tcp://127.0.0.1:5680")

# Run a simple "Echo" server
while True:
    message = repsock.recv()
    #message = message.decode()
    #message = message[::-1]
    #repsock.send_string("Echo: " + message)
    pubsock.send(message)
    #print("[Server] Echo: " + message)