__author__ = 'xiuchengquek'

import zmq
from rna_distance import match_sample_to_structure
import sys



reciever_ip = 'tcp://192.168.11.203:5559'
sinker_ip = 'tcp://192.168.11.203:5558'
context = zmq.Context()

# Get reciever
receiver = context.socket(zmq.PULL)
receiver.connect(reciever_ip)

sinker = context.socket(zmq.PUSH)
sinker.connect(sinker_ip)

while True:
    data = receiver.recv_json()
    sample_file = data['sample_file']
    structure_file = data['structure_file']
    out_dir = data['out_dir']
    match_sample_to_structure.match_sample_to_structure(sample_file, structure_file, out_dir)

    sys.stdout.write('working on %s\n' % sample_file)
    sys.stdout.flush()

    sinker.send_json({
        'sender' : 'worker',
        'body' : "%s\tcompleted" % structure_file
    })



