__author__ = 'xiuchengquek'

import os


def filename_to_parameters(filename) :
    filename = filename.replace('data/out/', '')
    filename = filename.replace('.results', '')
    parameters = filename.split('_')

    # score is in the following array 0 - k, 1 - t, 2 - o , 3 - e
    parameters = [ x.split('-')[-1] for x in parameters]
    return parameters


def match_sample_to_structure(sample_file, structure_file, out_dir):
    structure_distance = parse_structure_file(structure_file)

    sample_name = os.path.basename(sample_file)
    alignment_pair = sample_name.replace('.rna_structures.tsv', '')
    alignment_pair = alignment_pair.replace(' ', '\t')

    outfile = os.path.join(out_dir, sample_name)
    fh_out = open(outfile, 'w+')

    with open(sample_file) as f:
        for line in f:
            line = line.strip()
            fields = line.split('\t')

            structure = fields[3]
            distance = structure_distance[structure]

            parameters = filename_to_parameters((fields[2]))
            parameters.insert(0, alignment_pair)
            parameters.append(structure)
            parameters.append(distance)

            fh_out.write("%s\n" % "\t".join(parameters))

    fh_out.close()

def parse_structure_file(structure_file):
    structure_score = {}
    with open(structure_file) as f:
        for line in f:
            line = line.strip()
            structure, distance  = line.split('\t')
            structure_score[structure] = distance

    return structure_score

