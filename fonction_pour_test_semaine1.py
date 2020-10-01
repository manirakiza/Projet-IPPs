import unittest
import semaine1_test as tf
mon_dict= {'A': ['B', 'C'], 'B': ['C', 'D'], 'D': ['E']}
fichier_test='D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt'
class TestOfFunction(unittest.TestCase):
    def test_read_interaction_file_dict(self):
        #"on vérifie que la focntion fonctionne "
      self.assertEqual(tf.read_interaction_file_dict(fichier_test),mon_dict)
    
