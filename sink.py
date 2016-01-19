__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'



import sys
import time
import zmq

from zeromq_rnadistance.sink import sink
from progressbar import ProgressBar , Percentage, Bar, RotatingMarker, ETA


sinker_ip = "tcp://*:5558"



class rnaDistanceSink(sink):

    def run(self):
        prg_bar = ProgressBar(widgets=[Percentage(), Bar(marker=RotatingMarker()), ETA()])
        i = 0
        total = 0
        while True:
            msg = self.receiver.recv()
            if msg['sender'] == 'ventilator':
                total = msg['total_count']
                prg_bar.maxval = total
                prg_bar = prg_bar.start()

            else:
                i += 1
                prg_bar.update(i)
                sys.stdout.write(msg['body'])
                sys.stdout.flush()



            if total == i :
                break

        prg_bar.close()














