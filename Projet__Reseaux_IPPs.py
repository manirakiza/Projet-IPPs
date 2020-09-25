##1.2.1 Question préliminaire(dictionnary of IPPs)
def read_interaction_file_dict(File):
    file_line=open(File,"r")
    nbre_ligne=int(file_line.readline()[:-1])
    dict_name={}
    for line in range(0, nbre_ligne-1):
        ligne = file_line.readline()[:-1]
        data = ligne.split()
        sommet_graphe1 = data[0]
        sommet_graphe2= data[1]
        if not(sommet_graphe1 in dict_name):
            dict_name[sommet_graphe1] = []
        dict_name[sommet_graphe1].append(sommet_graphe2)
        line +=1
    return dict_name
print("---------mon dictionnaire-----------")

rs = read_interaction_file_dict("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt")
print("\nMon dict {}".format(rs))
#[(A,B),(A,C),(B,C),(B,D),(D,E),(D,F)]
# #1.2.2 Question préliminaire (list of IPPs)
def read_interaction_file_list(File1):
    file_line=open(File1,"r")
    number_line=int(file_line.readline()[:-1])
    vertex=[]
    for line in range(0,number_line):
        line=file_line.readline()[:-1]
        if line:
            data=line.split()
            sommet_graphe1=data[0]
            sommet_graphe2=data[1]
            tuples=(sommet_graphe1,sommet_graphe2)
            vertex.append(tuples)
    file_line.close()
    return vertex
print("---------ma liste ----------")
print("")
print(read_interaction_file_list("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))
  
##1.2.4 Question préliminaire
def read_interaction_file(File2):
    return(read_interaction_file_dict(File2),read_interaction_file_list(File2))
print("-------ma liste et dictionnaire------")
print("")
print(read_interaction_file("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

##1.2.7 Question test
def is_interaction_file(File3):
    file_test=open(File3,"r")
    line_number=int(file_test.readline()[:-1])
    boolean_val="false"
    nombre_inter=0
    for val in range(0,line_number):
        line_inter=file_test.readline()[:-1]
        print(line_inter)
        if len(line_inter)==2:
            boolean_val="true"
        nombre_inter =val+1
        val +=1
    if line_number==nombre_inter:
        boolean_val="true"
    return boolean_val
            
print(is_interaction_file("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

        
    
    