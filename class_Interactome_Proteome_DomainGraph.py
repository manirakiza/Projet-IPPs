import urllib.request
import csv
import pickle
import matplotlib.pyplot as plt
import os
import re
import tempfile
                ##=============================================#
                ##=======   Classe INTERACTOME        =========#
                ##=============================================#
class Interactome:
    str_dico={}
    str_list=[]
    prot_dico={}
    proteins=[]
    def __init__(self,file):
        self.str_dico=self.read_interaction_file_dict(file)
        self.str_list=self.read_interaction_file_list(file)
        self.prot_dico=self.protId_file_dict(file)
        self.proteins=self.proteins_list()
    #Q 1.2.1 du chapitre 1
    def read_interaction_file_dict(self,file):
        #Desctiption de la fonction:
        #--------------------------
        #Fonction qui a pour but de stocker le graphe d'interactions(proteine-proteine) dans un dictionnaire où les clés sont les sommets
        #et leurs valeurs associées aux clés sont les sommets voisins.
        #La fonction retourne un dictionnaire d'interaction proteine-proteine
        file_line=open(file,"r")
        file_line.readline()        #première ligne du fichier correspondant au nombre d'interactions(proteine-proteine)
        str_dict={}                  #dictionnaire dans lequel on va stocker les interactions
        for str_ligne in file_line.readlines():   #boucle pour parcourir toutes les lignes du fichier
            data = str_ligne.split()              #chaque ligne est composée de deux proteines sparées par espace          
            sommet1= data[0]                      #premiere proteine pour chaque ligne
            sommet2= data[1]                      #Deuxieme proteine voisine de la première proteine 
            if not(sommet1 in str_dict.keys()):   #premiere proteine est une clé dont sa valeur est la deuxième proteine voisine
                str_dict[sommet1] = []            
                str_dict[sommet1].append(sommet2)
            else:
                str_dict[sommet1].append(sommet2)
            if not(sommet2 in str_dict.keys()):     #deuxième proteine peut devenir une clé dont sa valeur est la proteine voisine
                str_dict[sommet2] = []
                str_dict[sommet2].append(sommet1)
            else:
                str_dict[sommet2].append(sommet2)
            
        file_line.close()                #on ferme le fichier
        return str_dict
    def read_interaction_file_list(self,file):
        #==============Description:
        #La fonction a pour but e stocker le graphe d'interactions(proteine-proteine) dans une liste
        #parametres d'entres:fichier de graphe d'interaction proteine-protein
        #parametres de sorties:liste d'un couple(sommet1,sommet2) où sommet1 represente la première proteine et sommet2 represente la deuxième proteine 
        #La fonction retourn une liste d'interactions proteine-proteine
        file_line=open(file,"r")
        file_line.readline()
        list_interaction=[]
        for str_ligne in file_line.readlines():
            inter_sommet=str_ligne.split()
            sommet1=inter_sommet[0]     #première proteine dans fichier de graphe d'interaction proteine-protein
            sommet2=inter_sommet[1]     ##deuxième proteine dans fichier de graphe d'interaction proteine-protein
            list_interaction.append((sommet1,sommet2)) #les deux sommets represente une interaction dans une liste
        file_line.close()
        return list_interaction
    
    def proteins_list(self) :
        #La fonction a pour but de retourner la liste des proteines du graphe
        #La fonction retourne une liste
        list_proteins = []
        for key in self.str_dico.keys() :
            proteins_list.append(key)
        return(list_proteins)
    #=====================================#
    #==========Semaine 2 =================#
    #=====================================#
    #Q 2.1.1 Question exploration
    def count_vertices(self):
        #======Description:
        #La fonction a pour but de calculer le nombre de sommet d'un graphe
        #La fonction retourne un nombre de sommet
        int_nbre_sommet=len(self.str_dico)      #correspond au nombre de clés du dictionnaire
        print("Nombre de sommet: ", int_nbre_sommet)
        return int_nbre_sommet
    #Q 2.1.2 Question exploration
    def count_edges(self):
        #==========Description:
        #La fonction a pour but de compter le nombre d’arêtes d’un graphe.
        #La fonction retourne une entier qui represente le nombre d'interaction proteine-proteine du graphe
        int_nbre_aretes= len(self.str_list) #La taille de la liste des interactions correspond au nombre d’arêtes d’un graphe
        return int_nbre_aretes
    #Q 2.1.3 Question nettoyage
    def clean_interactome(self,file):
        #=========Descriptions:
        #La fonction a pour but d'enlèver toutes les interactions redondantes, et
        #tous les homo-dimères.
        #parametres d'entre:fichier contenant un graphe d’interactions protéine-protéine
        outfile=open(("D:/BS2/Human_HighQuality_clean.txt"),"w")
        Nouv_list_inter=[]             #Nouveau liste d'interaction
        for interaction in self.str_list:
            nouveau_inter=(interaction[1],interaction[0]) #cas ou la première proteine devient la deuxième proteine et vice versa dans un fichier de graphe d'interactions
            if interaction not in Nouv_list_inter:    
                if nouveau_inter not in Nouv_list_inter:
                    if interaction[0]!=interaction[1]:       #lorsque les deux proteines ne sont pas identiques
                        Nouv_list_inter.append(interaction)  #nouveau liste sans interactions redondantes et tous les homo-dimères
        int_nb_interaction= str(len(Nouv_list_inter))             #Nombre d'interaction
        outfile.write(str(int_nb_interaction +'\n'))         #première ligne du fichier
        for nouv_int in Nouv_list_inter:
            nouv_interacion=' '.join(nouv_int)
            outfile.write(str(nouv_interacion + '\n'))       #Nouvelles interactions des proteines
    #Q 2.2.2 Question degré
    def get_max_degree(self,file):
        #=========Description:
        #La fonction a pour but de determiner le nom de la protéine de degré
        #maximal ainsi que le degré de cette protéine
        #parametre d'entree:fichier d'interaction proteine-proteine
        #La fonction retourne la protéine de degrémaximal ainsi que le degré de cette protéine
        max_deg = ("", 0) 	# intialisation de la variable qui stockera la proteine et son degre maximal
        for sommet in self.str_dico:		#on cherche dans tous les sommets du graphe 
    	    int_deg = len(self.str_dico[sommet])	# degre de la proteine cherche dans le dictionnaire
    	    if int_deg > max_deg[1]:		# comparaison avec le degre initiale
    	        max_deg = (sommet, int_deg)		#variable initiale prend le degre et la proteine correspondante
    	    if (int_deg == max_deg[1]) & (sommet!= max_deg[0]) :   
    	        max_deg = max_deg+ (sommet, int_deg)		# proteine et son degre associe
        return max_deg
    #====================================#
    #===========Semaine 4 ===============#
    #====================================#
    
    def count_cc(self):
        #La fonction a pour but de calculer le nombre de composantes connexes d’ungraphe, et donne pour chacune d’elle sa taille
        #La fonction retourne un dictionnaire
        dico = {}
         prot_list = list(self.proteins) #liste de toutes les proteines non redondantes
        int_cle = 1
        while len(prot_list) != 0:  #tant que la liste n'est pas vide on essaie de chercher  les composantes connexes
            dico[int_cle] = [prot_list[0]]
            for str_prot1 in dico[int_cle]:
                for str_prot2 in self.str_dico[str_prot1]:
                    if (str_prot2 not in dico[int_cle]) & (str_prot2 in prot_list):
                        dico[int_cle].append(str_prot2)
                        prot_list.remove(prot2_str)
                if str_prot1 in prot_list:
                    prot_list.remove(str_prot1)
            int_cle = int_cle + 1
        for int_cle in dico:
            dico[int_cle] = (len(dico[int_cle]), dico[int_cle])
        return dico
    def extractCC(self,prot):
        #L a fonction a pour but de derminer tous les sommets de la composante connexe de protteine donnée(prot)
        #L a fonction retourne une liste
        list_connexe = [prot]
        for key in list_connexe  :
            #pour la proteine donnee on regarde s'il existe dans le fichier d'interactome
            if prot not in self.proteins:
                    print("la proteine n'existe pas")
            else:
                #la proteine existe on regarde dans le dictionnaire des proteines s'elle existe et on cherche son proteine voisine voisin
                for prot_cc in self.str_dico[key]:
                    if prot_cc not in list_connexe  :
                        list_connexe .append(prot_cc)
        return list_connexe 
    def write_cc(self):
        #=========Description:
        #La fonction a pour but qui d'écrire dans un fichier les différentes composantes connexes d’un graphe
        #La fonction retourne un fichier
        nouveau_file = open("D:/BS2/fichier_comp_connexe.text", "x") #chemin de stockage du nouveau fichier
        cc_dico = self.count_cc()
        for cle in cc_dico:
            nouveau_file.write(str(cc_dico[cle][0]) + " " + str(cc_dico[cle][1]) + "\n")
        nouveau_file.close()
    #Q 4.2.1 Question densité
    def density(self):
        dens_float = (2*len(self.str_list))/(len(self.proteins_list())*(len(self.proteins_list())-1))
        print("La densite du graphe est : ", dens_float)
        return dens_float
    #Q 4.2.2 Question coefficient de clustering
    def clustering(self, prot):
        #===========Description:
        #La fonction a pour but de calcurer le coefficient de clustering de la protein donne
        #parametre : (prot) proteine dont on cherche son coefficient de clustering
        #La fonction retourne coeffcient de type float
        int_degre = self.get_degree(prot) #degre de la proteine donne
        cluster_coef_float = 0               #initialisation du coefficient de clustering
        if degree_int > 1:
            int_voisin_prot = 0               
            for str_voisin1 in self.str_dico[prot]: 
                for str_voisin2 in self.str_dico[str_voisin1]:
                    if str_voisin2 in self.str_dico[prot]:
                        int_voisin_prot = int_voisin_prot + 1
            cluster_coef_float = int_voisin_prot/(int_degre*(int_degre-1))
        else:
            print("le coefficient de clustering", prot_int, " : ", cluster_coef_float)
        return cluster_coef_float
# fichier="D:/BS2/Data/proteine.txt"
# prot=Interactome(fichier)
# print(prot.read_interaction_file_dict(fichier))
    def protId_file_dict(self,file):
        #Description de la fonction:
        #---------------------------
        #cette focntion a pour but de créer un dictionnaire stockant les noms des protéines comme clés et les identifiants associés comme valeurs
        str_line=open(file,"r")
        str_line.readline()
        prot_dict={}
        for line in str_line.readlines():
            data = line.split()
            idprot = data[0]
            nameprot= data[3]
            print(nameprot)
            if not(nameprot in prot_dict.keys()):
                prot_dict[nameprot] = []
                prot_dict[nameprot].append(idprot)
        str_line.close()
        return prot_dict
     #Q6 duchapitre 5
    def xlinkUniprot(self,fichier):
        #Description de la focntion:
        #---------------------------
        #Cette fonction a pour but d'etendre le dictionnaire en stockant une proteine,son identifiant et les proteines voisins
        #Fichier d'entree contient 5 colonnes : Entry	Protein names	Gene names	Length	Entry name
        dict_graphe = {}        #dictionnaire de l'interaction proteine-identifiant et poteines voisines
        #str_id=Proteome(fichier)
        file="D:/BS2/Data/proteine.txt"
        prot_dico=self.protId_file_dict(fichier)
        str_dico=self.read_interaction_file_dict(file)
        for nom_prot in str_dico.keys(): # proteines definies comme clés dans le Dictionnaire (interaction proteine proteine du chapitre 1)
            if nom_prot in prot_dico: 
                dict_graphe[nom_prot]={}
            dict_graphe[nom_prot]["UniprotID"]=prot_dico[nom_prot]
            dict_graphe[nom_prot]["voisins"]=str_dico[nom_prot]
        return dict_graphe
#      #5.4.2 Question 8
    def get_protein_domains(self,p):
        #==========Description:
        # Cette fonction a pour but de chercher le(s) domaine(s) contenus pour la proteine p dans la page Uniprot correspondant
        #La fonction retourne une liste de domaines de la proteine p
        #id_uniprot=self.prot_dico.values()
        #print(id_uniprot)
        url="https://www.uniprot.org/uniprot/{}.txt".format(p)
        with urllib.request.urlopen(url) as reponse:
            with tempfile.TemporaryFile() as fich_temp:
                shutil.copyfileobj(reponse, fich_temp)
                fich_temp.write(reponse.read())
                fich_temp.seek(0)
                #exemple de lignes correspondantes dans lesquelles on extrait les domaines:
                #DR   Pfam; PF00757; Furin-like; 1.
                domains = re.findall(r'DR\s{3}Pfam; \w+; [\w\-]+; \d+', str(reponse.read()))
                print(domains)
                dico_domains= {}
                list_domains=[]
                for dom in domains:
                    caracteritiques = dom.split("; ")
                    dico_domains[caracteritiques[2]]=int(caracteritiques[3])
                for key, value in dico_domains.items():
                    list_domains.append([key]*value)
                return(list_domains)
                fich_temp.close()
    #5.4.3 Question 9
    def xlink_domains(self):
        #======Description:
        #Cette fonction a pour but de créer et étendre un dictionnaire en ajoutant les domaines aux proteines
        #La fonction retourne un dictionnaire
        dict_graphe=self.dict_graphe
        fich_prot_domain=open("D:/BS2/Data/pro_voisins_domaines.pickle","r")
        for cle in self.dict_graphe.keys():
            self.dict_graphe[cle]["domains"]=self.get_protein_domains(cle)
            pickle.dump(dict_graphe, f )
        return dict_graphe
    #Q 6.2.1 Question liste des protéines
    def ls_proteins(self):
        #=== description:
        #La fonction a pour but de créer une liste de tous les proteines non redondantes de l'interaction proteine-proteine
        #elle retourne une liste de proteines
        list_prot=[]
        for protein in self.dict_graphe.keys():
            list_prot.append(protein)
        return list_prot
    #Q 6.2.2 Question liste des domaines  
    def ls_domains(self):
        #=======Description:
        #La fonction a pour but de creéer une listes des domaines non redondants qu'on trouve
        #dans proteines ,elle retrourne une liste de proteines
        fich_domaines=open("D:/BS2/Data/prot_protvoisins_domaines.pickle","r")
        list_domaines=[]                   #disctionnaire pour stocker les domaines
        dico_proteome=pickle.load(fich_domaines)
        for prot in dico_proteome.keys():
            print(prot)
            domains=dico_proteome[prot]["domains"]
            for dom in domains:
                if dom not in list_domaines:
                    list_domaines.append()
        fich_domaines.close()
        return list_domaines
    #print(ls_domains("D:/BS2/Data/prot_protvoisins_domaines.pickle"))
    #6.2.3 Question liste des domaines
    def ls_domains_n(self,n):
        #======Description:
        #La fonction a pour but de créer une liste de tous les domaines non redontants
        #que l’on trouve au moins (n) fois dans les protéines
        list_domaine_repet=[]
        domaines_rep=open("D:/BS2/Data/Domaines.pickle","r")
        dico_domaines_rep=pickle.load(domaines_rep)
        for cle in dico_domaines_rep.keys():
            for val in dico_domaines_rep.values():
                if val >= n:
                    list_domaine_repet.append(cle)
        domaines_rep.close()
        return list_domaine_repet
    #6.2.4 Question distribution du nombre de domaines par protéine
    def nbDomainsByProteinDistribution(self):
        #==============Description:
        #La fonction a pour but de creer un dictionnaire stockant la distribution des domaines
        #par domaines,elle retourne une dictionnaire qui a clé comme nombres de domaines qu'on trouve dans les proteines
        # et les valeurs associees comme le nombre de protéines comportant ce nombre de domaines.
        domaines_par_prot={}
        compt_domaine=[]
        domaines_voisins=open("D:/BS2/Data/prot_voisins_domaines_nonredondant.pickle","r")
        dico_domaines_voisin=pickle.load(domaines_voisins)
        for protein in dico_domaines_voisin.keys():
            compt_domaine.append(dico_domaines_voisin[protein]["domains"])
            compt_domain=count(compt_domaine)
            domaines_par_prot=compt_domain
            domaines_par_prot=sorted(domaines_par_prot.items())
        domaines_voisins.close()
        return domaines_par_prot
    
    #6.2.5 Question distribution du nombre de protéines par domaine
    def nbProteinsByDomainDistribution(self):
        #========Description:
        #La fonction a pour but de creér un dictionnaire stockant nombres de protéines associées
        #à un domaine comme clé et les valeurs associés le nombre de domaines présents dans ce nombre de protéines
        prot_par_domaines={}
        domain_par_prot=self.nbDomainsByProteinDistribution()
        for cle in domain_par_prot.keys():
            prot_par_domaines[domain_par_prot[cle]]=cle
        return prot_par_domaines
      
    #Q 6.2.6 Question co-occurrence des domaines (1)
    def co_occurrence(self,dom_x,dom_y):
        #============Description:
        #La fonction a pour but de calculer le nombre de co-occurrences des domaines dans les proteines d'interactome.
        #parametres:
        #dom_x:nom du domaine x 
        #dom_y:nom du domaine y
        compt_occur=0
        #si le les deux domaines sont différents 
        if dom_x!=dom_y:
            for prot in self.str_dico:
                if dom_x in self.str_dico[prot]["domains"]:
                    if dom_y in self.str_dico[prot]["domains"]:
                        compt_occur=compt_occur+1
        return compt_occur
    #Q 6.2.16
    def weighted_cooccurrence_graph(self,coocc_min):
        #=================Description:
        #La fonction a pour but de créer un nouveau objet dont le grapphe de domaines est pondéré  
        #et ces  domaines sont co-occurrents.
        #parametre:coocc_min est le nombre de co_occurence minimal de domaines
        #La fonction retourne un nouveau objet de graphe de domaine
        fich=open("D:/BS2/Data/graphe.csv","w") #fichier .csv à generer 
        dom_graph_pondere=[]
        graph_dom=DomainGraph()
        list_dom_graph_n=graph_dom.generate_cooccurrence_graph_n(coocc_min)
        list_dom_graph_np=graph_dom.generate_cooccurrence_graph_np(coocc_min)
        list_dom_graph=graph_dom.generate_cooccurrence_graph()
        for inter in list_dom_graph_n:
            co_occur=self.cooccur_twodomains(inter[0],inter[1])   #cooccurence de domaines plusieurs fois dans les domaines
            dom_graph_pondere.append(inter,co_occur)
            genere-fich.write(inter[0]+";"+inter[1]+";"+str(co_occur)+"\n")
        genere-fich.close()
        return graph_dom
    ##========================================================================##
    ##========       Classe PROTEOME     =====================================##
    ##========================================================================##
#class Proteome:
    id_dico={}
    prot_dico={}
    def __init__(self,file):
        self.id_dico=self.idProt_file_dict(file)
        self.prot_dico=self.protId_file_dict(file)
    #On recupere les identifiants et les proteines dans le fichier de proteome humain
    #Q 5.3.3 Question 5 du chapitre 5
    ##Dictionnaire qui a comme clé nom de protéine et comme valeur l'identifiant
    def protId_file_dict(self,file):
        #Description de la fonction:
        #---------------------------
        #cette focntion a pour but de créer un dictionnaire stockant les noms des protéines comme clés et les identifiants associés comme valeurs
        str_line=open(file,"r")
        str_line.readline()
        prot_dict={}
        for line in str_line.readlines():
            data = line.split()
            idprot = data[0]
            nameprot= data[3]
            if not(nameprot in prot_dict.keys()):
                prot_dict[nameprot] = []
                prot_dict[nameprot].append(idprot)
        str_line.close()
        return prot_dict
    #Dictionnaire qui a comme clé l'identifiant et comme valeur nom de la proteine
    def idProt_file_dict(self,file):
        #========Description:
        #Cette focntion a pour but de créer un dictionnaire stockant les identifiants des proteines comme clés et les nomes des proteines associés comme valeurs
        str_line=open(file,"r")
        str_line.readline()
        id_dict={}              #dictionnaire stockant les identifiants des proteines comme clés et les nomes des proteines associés comme valeurs
        for line in str_line.readlines():
            data = line.split()
            idprot = data[0]         #identifiant dans le fichier du proteome humain
            nameprot= data[1]        #noms des proteines associés 
            if not(idprot in id_dict.keys()):
                id_dict[idprot] = []             #Les identifiants sont définis comme clés dans le dictionnaire
                id_dict[idprot].append(nameprot)  #Les noms des proteines associés sont définis comme valeurs dans le dictionnaire
        str_line.close()
        return id_dict
# fichier="D:/BS2/Data/proteome-Humain.txt"
# prot=Proteome(fichier)
# print(prot.protId_file_dict(fichier))
    ##========================================================================##
    ##========       Classe DOMAINGRAPH    ===================================##
    ##========================================================================##

 #Nouvelle structure : les graphes de domaines.
class DomainGraph:
    
    def __init__(self):
        self.domains_dict = {}
        self.dict_graphe=self.xlink_domains()
        self.list_domaines=self.ls_domains()
    #      #5.4.2 Question 8
    def get_protein_domains(self,id_uniprot):
        #==========Description:
        # Cette fonction a pour but de chercher le(s) domaine(s) contenus pour la proteine p dans la page Uniprot correspondant
        #La fonction retourne une liste de domaines de la proteine p
        #id_uniprot=self.prot_dico.values()
        #print(id_uniprot)
        url="https://www.uniprot.org/uniprot/"+id_uniprot+".txt"
        with urllib.request.urlopen(url) as reponse:
            with tempfile.TemporaryFile() as tmp_file:
                tmp_file.write(reponse.read())
                #exemple de lignes  dans lesquelles on extrait les domaines:
                #DR   Pfam; PF00757; Furin-like; 1.
                list_domains = re.findall(r'DR\s{3}Pfam; \w+; [\w\-]+; \d+', str(tmp_file.read()))
                print(list_domains)
                dico_domains= {}
                for dom in list_domains:
                    dom_propr = dom.split("; ")
                    dico_domains[dom_propr[2]]=int(dom_propr[3])
                return(dico_domains)
                fich_temp.close()
    
    #Q 6.2.2 Question liste des domaines  
    def ls_domains(self):
        #=======Description:
        #La fonction a pour but de creéer une listes des domaines non redondants qu'on trouve
        #dans proteines ,elle retrourne une liste de proteines
        fich_domaines=open("D:/BS2/Data/pro_voisins_domaines.pickle","r")
        list_domaines=[]                   #disctionnaire pour stocker les domaines
        dico_proteome=pickle.load(fich_domaines)
        for prot in dico_proteome.keys():
            print(prot)
            domains=dico_proteome[prot]["domains"]
            for dom in domains:
                if dom not in list_domaines:
                    list_domaines.append(dom )
        fich_domaines.close()
        return list_domaines
    def xlink_domains(self):
        #======Description:
        #Cette fonction a pour but de créer et étendre un dictionnaire en ajoutant les domaines aux proteines
        #La fonction retourne un dictionnaire
        dict_graphe=self.dict_graphe
        fich_prot_domain=open("D:/BS2/Data/pro_voisins_domaines.pickle","r")
        for cle in self.dict_graphe.keys():
            self.dict_graphe[cle]["domains"]=self.get_protein_domains(cle)
            pickle.dump(dict_graphe, f )
        return dict_graphe
    #6.2.7 Question co-occurrence des domaines (2)
    def generate_cooccurrence_graph(self):
        #===============Descriptionn:
        # La fonction a pour but de créer un graphe des co-occurrences entre domaines et l'interaction
        #entre domaines (lorsque ces domaines sont co-occurrents au moins dans une protéine du graphe).
        #la fonction retourne une liste d'interaction de domaines
        list_co_occur_graphe=[]
        #liste des domaines
        for dom1 in self.list_domaines:
            for prot in self.domains_dict[domain1]['proteins']:  #pour chaque domaine et proteine associée
                for dom2 in self.str_dico[prot]['domains']:   #pour chaque proteine et domaine associé
                    if dom1!=dom2 :
                        if (dom1,dom2) not in list_co_occur_graphe:   
                            if (dom2,dom1) not in list_co_occur_graphe:
                                dico_co_occur_graphe.append((dom1,dom2))  
        return list_co_occur_graphe
    #6.2.13 Question co-occurrence des domaines (3)
    def generate_cooccurrence_graph_np(self,n):
        #===============Description:
        #La fonction a pour but de chercher les co-occurrences fréquentes avec (n) minimum de co-occurrences,la fonction retourne une liste de domaines dont
        #les co-occurrences fréquentes 
        list_co_occur_graphe=[]
        #liste des domaines
        for dom1 in self.list_domaines:
            for prot in self.domains_dict[domain1]['proteins']:  #pour chaque domaine et proteine associée
                for dom2 in self.str_dico[prot]['domains']:   #pour chaque proteine et domaine associé
                    if dom1!=dom2 :
                        if (dom1,dom2) not in list_co_occur_graphe:   
                            if (dom2,dom1) not in list_co_occur_graphe:
                                if (self.co_occurrence(dom1,dom2)>=n):
                                    list_co_occur_graphe.append((dom1,dom2))       
        return list_co_occur_graphe
                    
                    
    def getocc_dom_by_prot(self,prot,dom):
        #============Description:
        #cette fonction a pour but de chercher le nombre d'occurence de domaine donne dans une proteine donne
        #La fonction retourne l'occurence
        occ=0
        if dom in self.str_dico[prot]['domains']:
            occ =occ+1
        return occ               #occurence retourné
    def cooccur_twodomains(self,domainx,domainy):
        #====Description:
        #Retourne le nombre max de cooccurence des domaines donnees
        #parametres entres:deux domaines
        coocc_max=0
        for prot in self.str_dico:
            if domainx!=domainy:
                int_n=self.getocc_dom_by_prot(prot,domainx)*self.getocc_dom_by_prot(prot,domainy)
                if int_n > coocc_max:
                    coocc_max = int_n
        return coocc_max
        
     
    #Q 6.2.16
    def generate_cooccurrence_graph_n(self,n):
        #===========Description:
        #La fonction a pour but de créer un graphe de domaines où ces domaines sont co-occurrents dans au moins n fois dans les protéines du graphe
        #parametre d'etree:nombre minimun(n) de co-occurence de domaines dans les proteines
        #parametre de sortie:liste d'interactions de domaines qui sont co-occurrents
        list_dom_grphe=[]
        for dom1 in self.list_domaines:
            for prot in self.domains_dict[dom1]['proteins']:
                for dom2 in self.str_dico[prot]['domains']:
                    if (dom1,dom2) not in list_dom-grphe:
                        if (dom2,dom1) not in list_dom-grphe :
                            if self.cooccur_twodomains(dom1,dom2):
                                list_dom-grphe.append(dom1,dom2)
        return list_dom-grphe
    
    def vertex_graphe(self):
        #======Description:
        #La fonction a pour but de determiner les sommets du graphe des domaines
        #parametre :liste de l'interaction(generate_cooccurrence_graph(self))
        #la focntion retourne une liste de sommets des domaines
        list_vertex=[]
        list_graphe=self.generate_cooccurrence_graph() #fonction qui retourne une interaction(domain-domain)
        for inter in list_graphe:      
            if inter[0] not in list_vertex: #si le premier domaine de l'interaction n'est pas dans la liste créee on l'ajoute
                list_vertex.append(inter[0])
            if inter[1] not in list_vertex: #si le 2éme domaine de l'interaction n'est pas dans la liste créee on l'ajoute
                list_vertex.append(inter[0])
        return list_vertex
    #Q 6.2.8 
    #clalcul de la densité du graphe
    def density(self):
        #===========Description:
        #La fonction a pour but de claculer la densite cest à dire le nombre d'interaction(aretes),par rapport
        #au nombre d’arêtes total qu’il pourrait théoriquement y avoir.
        #La fonction retourne un nombre de type double
        int_nombre_inter=len(self.self.generate_cooccurrence_graph()) #nombre d'interaction dans le graphe des domaines
        int_nombre_sommet=len(self.vertex_graphe())                  #nombre de sommet dans le graphe des domaines
        int_arete_existant=2*int_nombre_inter
        int_arete_theorique=int_nombre_sommet/(int_nombre_sommet-1)
        float_densite=int_arete_existant/int_arete_theorique
        return float_densite
    #Q 6.2.9 Question topologie (2)
    def dom_voisins(self,domain):
        #==========Description:
        #La fonction a pour but de chercher des domaines voisins d'un domain donné
        #La fonction retourne une liste de domaines voisin d'un domaine donné
        dom_voisins=[]
        for prot in self.domains_dict[domain]['proteins']:
            for dom in self.str_dico[prot]['domains'].keys():
                if self.getocc_dom_by_prot(prot,dom)>=2:
                    if (dom==domain) or (dom!=domain):
                        dom_voisins.append(dom)
        return dom_voisins
        
    def max_dom_voisins(self,nbre_max):
        #========Description:
        #La fonction a pour but de déterminer les 10 domaines ayant le plus grand nombre de voisins
        #Parametre:(nbre_max)nombre-maximal estimé de domaines voisins d'un domaine 
        #la fonction retourne une liste de ces domaines
        list_dom_voisins=[]
        for dom in self.list_domaines:
            if dom not in list_dom_voisins:
                if len(self.domains_dict[dom]['neighbors']) > nbre_max:
                    list_dom_voisins.append(dom)
        return list_dom_voisins
                    
            
    def min_dom_voisins(self,nbre_min):
        #========Description:
        #La fonction a pour but de déterminer les 10 domaines ayant le plus petit nombre de voisins
        #la fonction retourne une liste de ces domaines
        #parametres:(nbre_min) nombre-manimal estimé de domaines voisins d'un domaine
        list_dom_voisins=[]
        for dom in self.list_domaines:
            if dom not in list_dom_voisins:
                if len(self.domains_dict[dom]['neighbors']) < nbre_min:
                    list_dom_voisins.append(dom)
        return list_dom_voisins
    def nbDomainsByProteinsDistribution(self):
        #=============Description:
        #cette fonction a pour but de déterminer la distribution du nombre de domaines par nombre de protéines
        #L fonction retourne un dictionnaire
        domain_par_protein_dict={}
        nb_domains=[]
        with open('D:/BS2/data/prot_voisins_domaines_nonredondant.pickle', 'rb') as domain_dict:
            # chargement à l'aide du module pickle du dictionnaire contenant nom proteine , id uniprot , proteines voisins and domains
            dico_proteome=pickle.load(domain_dict)
            for protein in dico_proteome.keys():
                nb_domains.append(len(dico_proteome[protein]["domains"]))
                count_dict = Counter(nb_domains)
                domain_par_protein_dict=count_dict
        domain_par_protein_dict=sorted(domain_par_protein_dict.items(), key=lambda t: t[0])
        return dict(domain_par_protein_dict)
    def hist_nbDomainsByProteinsDistribution(self):
        #============Description:
        #Cette fonction a pour but de represent la distribution du nombre de domaines par nombre de protéines à l'aide de lhistogramme
        domain_par_protein_dic=self.nbDomainsByProteinsDistribution()
        plt.bar(list(domain_par_protein_dic.keys()), domain_par_protein_dic.values(), color='g')
        plt.title("Distribution in number of domains in function in number protein")
        plt.title("La distribution du nombre de domaines par nombre de protéines ")
        plt.xlabel("Nombre de domaines ")
        plt.ylabel("Nombre de proteines")
        plt.show()

    

                  
                
            
    
            
            
        
            
            

        
        

            
    
            
            
            
        
   
        
          
