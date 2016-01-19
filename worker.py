

from rna_distance import run_distance
from zeromq_rnadistance.worker import taskWorker
import sys

reciever = 'tcp://localhost:5557'
sender = 'tcp://localhost:5558'

class rnaDistWorker(taskWorker):
    def run(self):
        while True:
            data = self.receiver.recv_json()
            ref = "this is %s" % data['ref']
            struct_file =  data['structure_file']
            alignment_pair = data['alignment_pair']

            structures = run_distance.read_structure_file(struct_file)
            run_distance.run_distance(ref, structures)

            # Send results to sink
            self.sender.send_json({
                'sender' : 'worker',
                'body' : "completed\t%s\n" % alignment_pair
            }
            )



if __name__ == '__main__' :
    worker = rnaDistWorker(reciever, sender)
    worker.run()




