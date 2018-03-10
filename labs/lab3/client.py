import zmq
import sys
from threading import Thread

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"

def sub():
    subsock=context.socket(zmq.SUB)
    subsock.setsockopt_string(zmq.SUBSCRIBE," ")
    subsock.connect("tcp://127.0.0.1:5680")
    while True:
        server_msg=subsock.recv()
        print('\n'+server_msg)

        
def push():
    sock = context.socket(zmq.PUSH)
    sock.connect("tcp://127.0.0.1:5555")
    usr=sys.argv[1]
    print("User ["+usr+"] Connected to the chat Server.")
    msg=input("[{}]>".format(usr))
    sock.send_string('['+usr+']>'+msg)

if __name__=='__main__':
    t1=Thread(target=push).start()
    t2=Thread(target=sub).start()
