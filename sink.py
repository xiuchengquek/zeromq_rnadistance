__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'



import sys
import time
import zmq




context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# Wait for start of batch
s = receiver.recv()

# Start our clock now


# Process 100 confirmations

for task_nbr in range(100):
    s = receiver.recv()
    sys.stdout.write(s)
    sys.stdout.flush()




