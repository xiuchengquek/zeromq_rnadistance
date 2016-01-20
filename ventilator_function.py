__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'


from zeromq_rnadistance.ventilator import ventilator

import os
import sys
import json
import zmq


reciever_id = 'tcp://*:5559'
sink_ip = 'tcp://localhost:5558'





def read_reference(reference_file):
    reference_structure = {}
    with open(reference_file) as f:
        for line in f:
            line = line.strip()
            fields = line.split('\t')
            alignment_pair  = "%s %s" % (fields[0], fields[1])
            reference_structure[alignment_pair] = fields[2]
    return reference_structure


def get_data_set(wd):
    data_set = os.listdir(wd)
    data_set = { x.replace('.rna_structures.tsv', '') : os.path.join(wd, x) for x in data_set if x.endswith('rna_structures.tsv')}
    return data_set


if __name__ == '__main__' :

    context = zmq.Context()

    # Get reciever
    sender = context.socket(zmq.PUSH)
    sender.bind(reciever_id)

    sinker = context.socket(zmq.PUSH)
    sinker.connect(sink_ip)


    data_set = get_data_set('data/completed/split_files_2/')
    reference_sequence = read_reference('data/reference/results_reference_structure_corrected.txt')
    assert set(data_set.keys()) == set(reference_sequence.keys())

    sinker.send_json({
        'sender' : 'ventilator',
        'body' : str(len(reference_sequence.keys()))
    })

    #print("Press Enter when the workers are ready: ")
    #_ = input()

    
    for key, values in reference_sequence.items():
        print(key)
        data_package = { 'alignment_pair' : key,
          'ref' : values ,
          'structure_file' : data_set[key]
          }

        sender.send_json(data_package)






