

from rna_distance import run_distance
from zeromq_rnadistance.worker import taskWorker
import sys
import zmq

reciever = 'tcp://localhost:5557'
sender = 'tcp://localhost:5558'

class rnaDistWorker(taskWorker):
    def run(self):
        while True:
            data = self.receiver.recv_json()
            ref = "this is %s" % data['ref']
            struct_file =  data['structure_file']
            alignment_pair = data['alignment_pair']
            print(alignment_pair)

            structures = run_distance.read_structure_file(struct_file)
            print(structures)
            run_distance.run_distance_pexpect(ref, structures)
            print('done')

    def run_with_poll(self):
        self.start_poll()
        while True:
            socks = dict(self.poller.poll(1000))
            if socks:
                if socks.get(self.receiver) == zmq.POLLIN:
                    print ("got message ")
                    data = self.receiver.recv_json(zmq.NOBLOCK)
                    ref = "this is %s" % data['ref']
                    struct_file =  data['structure_file']
                    alignment_pair = data['alignment_pair']
                    print(alignment_pair)

                    structures = run_distance.read_structure_file(struct_file)
                    print(structures)
                    run_distance.run_distance_pexpect(ref, structures)
                    print('done')
            else:
                print('still watiing')





            # Send results to sink




if __name__ == '__main__' :
    worker = rnaDistWorker(reciever, sender)
    worker.run_with_poll()




