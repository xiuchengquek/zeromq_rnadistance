__author__ = 'xiuchengquek'

import sys
import time
import zmq

class sink:
    def __init__(self, receiver_ip):
        # Get context
        context = zmq.Context()

        # Get reciever
        receiver = context.socket(zmq.PULL)
        receiver.connect(receiver_ip)
        self.receiver = receiver

    def run(self):
        pass






