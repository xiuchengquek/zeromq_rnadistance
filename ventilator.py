__author__ = 'xiuchengquek'


from zeromq_rnadistance.ventilator import ventilator

import os
import sys
import json
reciever = 'tcp://localhost:5557'
sender = 'tcp://localhost:5558'








class rnaDistVentilator(ventilator):

    def read_reference(self, reference_file):
        reference_structure = {}
        with open(reference_file) as f:
            for line in f:
                line = line.strip()
                fields = line.split('\t')
                alignment_pair  = "%s %s" % (fields[0], fields[1])
                reference_structure[alignment_pair] = fields[2]
        return reference_structure


    def get_data_set(self, wd):
        data_set = os.listdir(wd)
        data_set = { x.replace('rna_structures.tsv', '') : os.path.join(wd, x) for x in data_set if x.endswith('rna_structures.tsv')}
        return data_set

    def run_rna_distance(self, reference_structure, structure_files):
        sys.stdout.write(reference_structure, structure_files)
        sys.stdout.flush()








    def run(self):
        print("Press Enter when the workers are ready: ")
        _ = input()

        data_set = self.get_data_set('data/completed/split_files/')
        reference_sequence = self.read_reference('data/reference/results_reference_structure_corrected.txt')

        ## check that all keys of reference_sequence are in data_set
        print(set(data_set.keys())- set(reference_sequence.keys()))
        sys.stdout.flush()

        assert set(data_set.keys()) == set(reference_sequence.keys())

        for key, values in reference_sequence.items():
            data_package = { 'alignment_pair' : key,
              'ref' : values ,
              'structure_file' : data_set[key]
              }

            self.sender.send_json(data_package)





if __name__ == '__main__' :
    rna_vent = rnaDistVentilator(reciever, sender)
    rna_vent.run()





