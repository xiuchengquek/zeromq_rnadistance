__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'
__author__ = 'xiuchengquek'


from zeromq_rnadistance.ventilator import ventilator

import os
import sys
import json
import zmq


reciever_id = 'tcp://*:5559'
sink_ip = 'tcp://localhost:5558'


if __name__ == '__main__' :


    wd = '/share/ClusterScratch/xiuque/martinSmith/data/completed/split_detailed'
    structure_dir = '/share/ClusterScratch/xiuque/martinSmith/data/rnadistance_results'
    out_dir = '/share/ClusterScratch/xiuque/marthinSmith/data/outdir/'

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
        structure_score_file = os.path.join(structure_dir, values)
        sample_file = os.path.join(wd, values)
        assert os.path.exists(structure_score_file)
        assert os.path.exists(sample_file)

        data_package = { 'alignment_pair' : values,
          'sample_file' : values ,
          'structure_file' : structure_score_file,
          'out_dir' : out_dir
           }

        sender.send_json(data_package)






