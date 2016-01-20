__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'

import sys
import time
import zmq
from rna_distance import run_distance

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
    ref = data['ref']
    struct_file =  data['structure_file']
    alignment_pair = data['alignment_pair']
    sys.stdout.write('working on %s\n' %alignment_pair)
    sys.stdout.flush()
    structures = run_distance.read_structure_file(struct_file)
    structures = set(structures)
   

    results = run_distance.run_distance_pexpect(ref, structures)
    out_file = "data/rnadistance_results/%s.rnadist.results.txt" % alignment_pair

    with open(out_file, 'w+') as f:
        for score in results:
            f.write("%s\n" % score)
   
    sinker.send_json({
        'sender' : 'worker',
        'body' : "%s\tcompleted" % alignment_pair


    })



