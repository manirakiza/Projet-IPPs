import unittest
import Projet

class TestOfFunction(unittest.TestCase):
    
    def test_interaction_file(self):
            interaction=Projet.Interaction("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt")
            interaction.read_interaction_file_dict()
            interaction.read_interaction_file_list()
            interaction.read_interaction_file()
            interaction.is_interaction_file()
            
    def test_calcul_degree(self):
        interaction=Projet.Interaction("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt")
        interaction.count_vertices()
        interaction.count_edges()
        interaction.clean_interactome()
        interaction.get_degree()
        interaction.get_max_degree()
        interaction.get_ave_degree()
        interaction.count_degree()
        interaction.histogram_degree()
        
    def test_composant_connexes(self):
        interaction=Projet.Interaction("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt")
        interaction.countCC()
        interaction.writeCC()
        interaction.extractCC()
        interaction.computeCC()
        interaction.density()
        interaction.clustering()    
if __name__ == '__main__':
    unittest.main()
