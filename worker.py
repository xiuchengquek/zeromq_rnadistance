

from zeromq_rnadistance.worker import taskWorker
import sys

reciever = 'tcp://localhost:5557'
sender = 'tcp://localhost:5558'

class rnaDistWorker(taskWorker):
    def run(self):
        while True:
            s = self.receiver.recv_json()
            results = "this is %s" % s['reference']
            # Send results to sink
            sys.stdout.write(results)
            sys.stdout.flush()
            self.sender.send_string(results)



if __name__ == '__main__' :
    worker = rnaDistWorker(reciever, sender)
    worker.run()




