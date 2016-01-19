__author__ = 'xiuchengquek'

import sys
import time
import zmq

class taskWorker:
    def __init__(self, receiver_ip, sender_ip):
        # Get context
        context = zmq.Context()

        # Get reciever
        receiver = context.socket(zmq.PULL)
        receiver.connect(receiver_ip)

        # Get Sender
        sender = context.socket(zmq.PUSH)
        sender.connect(sender_ip)

        self.sender = sender
        self.receiver = receiver

    def run(self):
        pass




