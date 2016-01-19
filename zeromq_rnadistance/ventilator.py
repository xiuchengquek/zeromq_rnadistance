__author__ = 'xiuchengquek'
# Task ventilator
# Binds PUSH socket to tcp://localhost:5557
# Sends batch of tasks to workers via that socket
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq
import random
import time

class ventilator:

    def __init__(self, sender_ip, sink_id):
             # Get context
        context = zmq.Context()

        # Get reciever
        sender = context.socket(zmq.PUSH)
        sender.connect(sink_id)

        # Get Sender
        sink = context.socket(zmq.PUSH)
        sink.connect(sink_id)

        self.sender = sender
        self.sink = sink


    def run(self):
        pass









