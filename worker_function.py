__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'

import sys
import time
import zmq
from rna_distance import run_distance

reciever_ip = 'tcp://localhost:5557'
sinker_ip = 'tcp://localhost:5558'
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
    structures = run_distance.read_structure_file(struct_file)
    results = run_distance.run_distance_pexpect(ref, structures)
    out_file = "data/rnadistance_results/%s.rnadist.results.txt" % alignment_pair

    with open(out_file, 'w+') as f:
        for score in results:
            f.write("where is a score %s\n" % score)

    sinker.send_json({
        'sender' : 'worker',
        'body' : "%s\tcompleted" % alignment_pair


    })



