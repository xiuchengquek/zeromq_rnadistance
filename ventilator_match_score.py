__author__ = 'xiuchengquek'


import os
import sys
import json
import zmq


reciever_id = 'tcp://*:5559'
sink_ip = 'tcp://localhost:5558'


if __name__ == '__main__' :


    wd = '/share/ClusterScratch/xiuque/martinSmith/data/completed/split_detailed'
    structure_dir = '/share/ClusterScratch/xiuque/martinSmith/data/rnadistance_results'
    out_dir = '/share/ClusterScratch/xiuque/martinSmith/data/outdir/'

    sample_file_list = os.listdir(wd)

    context = zmq.Context()

    # Get reciever
    sender = context.socket(zmq.PUSH)
    sender.bind(reciever_id)

    sinker = context.socket(zmq.PUSH)
    sinker.connect(sink_ip)

    sinker.send_json({
        'sender' : 'ventilator',
        'body' : str(len(sample_file_list))
    })

    for values in sample_file_list:
        structure_file_name = values.replace('.rna_structures.tsv', '.rnadist.results.txt')
        structure_score_file = os.path.join(structure_dir, structure_file_name)

        sample_file = os.path.join(wd, values)
        assert os.path.exists(structure_score_file) , "structure file missing %s" % structure_score_file
        assert os.path.exists(sample_file) , "sample_file file missing %s" % sample_file
        assert os.path.exists(out_dir) , "out_dir file missing %s" % out_dir


        data_package = { 'alignment_pair' : values,
          'sample_file' : sample_file ,
          'structure_file' : structure_score_file,
          'out_dir' : out_dir
           }

        sender.send_json(data_package)






