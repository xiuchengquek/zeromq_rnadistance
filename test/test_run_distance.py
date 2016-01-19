__author__ = 'xiuchengquek'


import unittest
from rna_distance import run_distance




class TestRunDistance(unittest.TestCase):


    def setUp(self):
        self.reference = '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))'
        self.structures = ['(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))',
                           '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))',
                           '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))',
                           '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))',
                           '(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))(((((((..((((.........)))).(((((.......)))).).....(((((.......))))))))))))']
    def testBasic(self):
        results = run_distance.run_distance(self.reference, self.structures)
        self.assertTrue(len(results), 5)
        print(results)


    def testPexpect(self):
        results = run_distance.run_distance_pexpect(self.reference, self.structures)
        self.assertTrue(len(results), 5)
        print(results)







