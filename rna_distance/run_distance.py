__author__ = 'xiuchengquek'





import subprocess


def read_structure_file(file):

    with open(file) as f:
        structure  = []
        for line in f:
            line = line.strip()
            fields = line.split('\t')
            structure.append(fields[-1])

    return structure


def run_distance(reference, structure):
    cmd = ['RNAdistance', '-Xf']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
    p.stdin.write(bytes("%s\n" % reference, 'UTF-8'))
    p.stdin.flush()

    results = []
    for struct in structure:
        print(struct)
        p.stdin.write(bytes("%s\n" % struct, 'UTF-8'))
        p.stdin.flush()
        res = p.stdout.readline()
        res = res.decode("utf-8")
        res = res.strip()
        res = res.replace('f: ','')
        res = "%s\t%s\n" % (struct, res)
        results.append(res)
    return results
















