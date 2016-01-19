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

    def __init__(self, sender_ip, sink_ip):
             # Get context
        context = zmq.Context()

        # Get reciever
        sender = context.socket(zmq.PUSH)
        sender.bind(sender_ip)

        # Get Sender
       # sink = context.socket(zmq.PUSH)
       # sink.connect(sink_ip)

        self.sender = sender
      #  self.sink = sink


    def run(self):
        pass









