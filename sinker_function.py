__author__ = 'xiuchengquek'



import zmq
import sys
from progressbar import ProgressBar , Percentage, Bar, RotatingMarker, ETA



receiver_ip = "tcp://*:5558"

context = zmq.Context()
# Get reciever
receiver = context.socket(zmq.PULL)
receiver.bind(receiver_ip)

prg_bar = ProgressBar(widgets=[Percentage(), Bar(marker=RotatingMarker()), ETA()])
i = 0

fh_out = open('data/logs/completed_rna_dist.log','w+')
while True:
    msg = receiver.recv_json()
    if msg['sender'] == 'ventilator':
        total = int(msg['body'])
        prg_bar.maxval = total
        prg_bar = prg_bar.start()
    else:
        i += 1
        prg_bar.update(i)
        fh_out.write('%s\n'  % msg['body'])
    if total == i :
        break

prg_bar.finish()
fh_out.close()
