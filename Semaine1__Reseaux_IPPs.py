##1.2.1 Question préliminaire(dictionnary of IPPs)
#Fonction qui stocke le graphe d'interactions dans un dictionnaire où les clés sont les sommets
#et les valeurs associées aux clés sont les voisins des sommets.

#Q 1.2.1 Question préliminaire
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
print("---------mon dictionnaire-----------")
rs = read_interaction_file_dict('D:/BS2/Human_HighQuality.txt')
print("\nMon dict {}".format(rs))

# #1.2.2 Question préliminaire (list of IPPs)
#Fonction qui stocke le graphe d'interaction dans une liste de couple.
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

#print(read_interaction_file_list('D:/BS2/Human_HighQuality.txt'))
##1.2.4 Question préliminaire
#Fonction qui retourne le dictionnaire et la liste
def read_interaction_file(file):
    #=============Description:
    #La fonction a pour but retourner le dictionnaire et la liste
    #parametre d'entree:fichier de graphe d'interaction proteine proteine
    d_int=read_interaction_file_dict(File2)
    l_int=read_interaction_file_list(File2)
    return(d_int,l_int)

#print(read_interaction_file('D:/BS2/Human_HighQuality.txt'))

##1.2.7 Question test
#Fonction pour vérifier si le fichier d'interactions est bien au format attendu
def is_interaction_file(file):
    #==========Description:
    #La fonction a pour objectif de vérifier que le fichier est bien au format attendu pour être lu correctement   
    file_line=open(file,"r")
    file_line.readline()
    file_line.readline() #première ligne du fichier correspondant au nbre de ligne
    nombre_ligne=0
    for str_ligne in file_line.readlines():
        data=str_ligne.split()
        if len(data)==2:            #Si la longueur de la ligne est egale à deux (deux proteine par ligne)
            nombre_ligne =nombre_ligne+1
    str_reponse=""
    if nombre_ligne!= line_number:
        str_reponse='false'
    elif len(data)>2 or len(data)<2:
        str_reponse='false'
    else:
        str_reponse='true'
    file_line.close()
    return str_reponse 
print(is_interaction_file('D:/BS2/Human_HighQuality.txt'))

