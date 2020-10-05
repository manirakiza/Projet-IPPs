##1.2.1 Question préliminaire(dictionnary of IPPs)
#Fonction qui stocke le graphe d'interactions dans un dictionnaire où les clés sont les sommets
#et les valeurs associées aux clés sont les voisins des sommets.
def read_interaction_file_dict(File):
    file_line=open(File,"r")
    nbre_ligne=int(file_line.readline()[:-1]) #première ligne du fichier correspondant au nombre d'interactions
    nom_dict={}
    line=0
    while line<nbre_ligne:
        ligne = file_line.readline()[:-1]
        data = ligne.split()
        sommet_graphe1 = data[0]
        sommet_graphe2= data[1]
        if not(sommet_graphe1 in nom_dict):
            nom_dict[sommet_graphe1] = []
        nom_dict[sommet_graphe1].append(sommet_graphe2)
        line +=1
    file_line.close()  
    return nom_dict
print("---------mon dictionnaire-----------")
rs = read_interaction_file_dict("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt")
print("\nMon dict {}".format(rs))

# #1.2.2 Question préliminaire (list of IPPs)
#Fonction qui stocke le graphe d'interaction dans une liste de couple.
def read_interaction_file_list(File1):
    file_line=open(File1,"r")
    number_line=int(file_line.readline()[:-1])
    list_sommet=[]
    line=0
    while line<number_line:
        line=file_line.readline()[:-1]
        if line:
            data=line.split()
            sommet_graphe1=data[0]
            sommet_graphe2=data[1]
            tuples=(sommet_graphe1,sommet_graphe2)
            list_sommet.append(tuples)
         line=line+1
    file_line.close()
    return list_sommet
print("---------ma liste ----------")
print("")
print(read_interaction_file_list("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))
  
##1.2.4 Question préliminaire
#Fonction qui retourne le dictionnaire et la liste
def read_interaction_file(File2):
    d_int=read_interaction_file_dict(File2)
    l_int=read_interaction_file_list(File2)
    return(d_int,l_int)
print("-------ma liste et dictionnaire------")
print("")
print(read_interaction_file("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

##1.2.7 Question test
#Fonction pour vérifier si le fichier d'interactions est bien au format attendu
def is_interaction_file(File3):
    file_test=open(File3,"r")
    line_number=int(file_test.readline()[:-1]) #première ligne du fichier correspondant au nbre de ligne
    nombre_ligne=0
    val=0
    while val < line_number:
        line_inter=file_test.readline()[:-1]
        data=line_inter.split()
        if len(data)==2:
            nombre_ligne =nombre_ligne+1
        val +=1
    print(nombre_ligne)
    str_reponse=""
    if nombre_ligne!= line_number:
        str_reponse='false'
    elif len(data)>2 or len(data)<2:
        str_reponse='false'
    else:
        str_reponse='true'
    return str_reponse 
     
print(is_interaction_file("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_examplev1.txt"))


        
    
    
