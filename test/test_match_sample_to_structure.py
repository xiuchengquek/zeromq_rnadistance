__author__ = 'xiuchengquek'


__author__ = 'xiuchengquek'

import os
import unittest
from rna_distance import match_sample_to_structure






class TestMatchSampleToStructure(unittest.TestCase):


    def setUp(self):
        structure_file_content = '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))\t0'
        self.structure_file = './test/structures/seqA seqB.rna_structures.tsv'
        self.structure_dir = './test/structures'
        details = 'seqA\tseqB\tdata/out/data/out/k-0.0_t-0.0_o-0.4_e-1.0.results\t(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))'
        self.details_file = './test/detail/seqA seqB.rna_structures.tsv'
        self.detail_dir = './test/detail'

        self.output = 'seqA\tseqB\t0.0\t0.0\t0.4\t1.0\t(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))\t0\n'
        self.out_dir = './test/out'
        self.out_file = './test/out/seqA seqB.rna_structures.tsv'

        os.mkdir(self.out_dir)
        os.mkdir(self.detail_dir)
        os.mkdir(self.structure_dir)

        with open(self.structure_file, 'w+') as f:
            f.write(structure_file_content)

        with open(self.details_file, 'w+') as f:
            f.write(details)




    def testBasic(self):

        match_sample_to_structure.match_sample_to_structure(self.details_file, self.structure_file, self.out_dir)
        self.assertTrue(os.path.exists(self.out_file))
        with open(self.out_file, 'r') as x:
            results = x.read()

        self.assertEqual(self.output, results)

    def tearDown(self):
        os.unlink(self.details_file)
        os.unlink(self.structure_file)
        os.rmdir(self.detail_dir)
        os.rmdir(self.structure_dir)
        os.unlink(self.out_file)
        os.rmdir(self.out_dir)






