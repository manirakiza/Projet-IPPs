#Semaine 2 : Exploration du graphe d’interactions protéine-protéine 
# Q1 Fonction pour compter compte le nombre de sommets d’un graphe.
def count_vertices(file):
    file_compte=open(file,"r") #lire un fichier 
    premier_ligne=int(file_compte.readline()[:-1]) #premier ligne correspondant au nombre d'interaction de fichier 
    int_nombre_sommet=0
    liste_sommet=[]
    i=0
    while i< premier_ligne:
        sommet_arret=file_compte.readline()[:-1]
        data=sommet_arret.split()
        if len(data)==2:
            liste_sommet.append(data[0])
            liste_sommet.append(data[1])
        i +=1
    #Liste des sommets du graphe 
    nouveau_liste=[]
    for sommet in liste_sommet:
        if not(sommet in nouveau_liste):
            nouveau_liste.append(sommet)
    #le nombre de sommet du graphe 
    int_nombre_sommet=len(nouveau_liste)
    print("La liste des sommets du graphe: ",nouveau_liste)
    print("Le nombre de sommets du graphe est :")
    file_compte.close()
    return int_nombre_sommet
print(count_vertices("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

# Version 2 meme fonction que la fonction prcedente
def count_vertices_v2(file):
    file=open(file,"r")
    number_line=int(file.readline()[:-1])
    liste=[]
    i=0
    while i<number_line:
        line=file.readline()[:-1]
        data=line.split()
        if len(data)==2:
            tuples=(data[0],data[1])
            liste.append(tuples) 
        i +=1
    nouveau_liste=[]
    for (sommet1,sommet2) in liste:
        if not sommet1 in nouveau_liste:
            nouveau_liste.append(sommet1)
        if not sommet2 in nouveau_liste:
            nouveau_liste.append(sommet2)
    int_nombre_sommet=len(nouveau_liste)
    print(nouveau_liste)
    file.close()
    return int_nombre_sommet
print(count_vertices('D:/BS2/Human_HighQuality.txt'))     

##Q2 Fonction pour compter  le nombre d’arêtes d’un graphe.
def count_edges():
    #fonction a pour objectif de compte le nombre d’arêtes(interaction) d’un graphe de proteines.
    liste=read_interaction_file_list('D:/BS2/Human_HighQuality.txt')
    nbre_aretes = len(liste) 
    return nbre_aretes
    
print(count_edges("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))
##Fonction pour eliminer toutes les interactions redondantes et tous les homo-dimères
##Fonction qui elimine les interactions redondantes et homo-dimères
def read_interaction_file_list(file):
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
def clean_interactome(file):
        #=========Descriptions:
        #La fonction a pour but d'enlèver toutes les interactions redondantes, et
        #tous les homo-dimères.
        #parametres d'entre:fichier contenant un graphe d’interactions protéine-protéine
        outfile=open(("D:/BS2/Human_HighQuality_clean.txt"),"w")
        liste=read_interaction_file_list('D:/BS2/Human_HighQuality.txt')
        Nouv_list_inter=[]             #Nouveau liste d'interaction
        for interaction in liste:
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
#Fonction pour calculer le degré d'une protéine donné dans le graphe.
def get_degree(file, prot):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    #nombre_arretes=0
    liste_tous_sommets=[]
    i=0
    while i<number_line:
        line=file_line.readline()[:-1]
        data=line.split()
        if len(data)==2:
            liste_tous_sommets.append(data[0])
            liste_tous_sommets.append(data[1])
        i=i+1
    print(liste_tous_sommets)
    dict_prot_degre={}
    for sommet in liste_tous_sommets:
        if sommet not in dict_prot_degre:
            dict_prot_degre[sommet]=1
        else:
            dict_prot_degre[sommet]=dict_prot_degre[sommet]+1
    #dictionnaire qui contient les protéines et leur dégré
    print("Le dictionnaire est ",dict_prot_degre)
    str_prot_de_deg=''
    int_deg=0
    for protein in dict_prot_degre.keys():
        if protein==prot:
            int_deg=int_deg+dict_prot_degre[protein]
            str_prot_de_deg=protein
    file_line.close()
    return(str_prot_de_deg,int_deg)
#print(get_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_v2.txt",A))
##Fonction pour retourner le dégré maximale et le nom d'une proteine 
def get_max_degree(file):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    #nombre_arretes=0
    liste_tous_sommets=[]
    i=0
    while i<number_line:
        line=file_line.readline()[:-1]
        data=line.split()
        if len(data)==2:
            liste_tous_sommets.append(data[0])
            liste_tous_sommets.append(data[1])
        i=i+1
    print(liste_tous_sommets)
    dict_prot_degre={}
    for sommet in liste_tous_sommets:
        if sommet not in dict_prot_degre:
            dict_prot_degre[sommet]=1
        else:
            dict_prot_degre[sommet]=dict_prot_degre[sommet]+1
    #dictionnaire qui contient les protéines et leur dégré
    print("Le dictionnaire est ",dict_prot_degre)
    str_prot_deg=''
    int_max_deg=max(dict_prot_degre.values())
    for prot in dict_prot_degre:
        if dict_prot_degre[prot]==int_max_deg:
            str_prot_deg=str_prot_deg+' '+prot
    file_line.close()
    print("proteine(s) qui a(ont) degre max =",int_max_deg, "est : ")
    return(str_prot_deg,int_max_deg)
print(get_max_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

##Fonction pour calculer le degré moyen des protéines du graphe.
def get_ave_degree(file):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    #nombre_arretes=0
    liste_tous_sommets=[]
    i=0
    while i<number_line:
        line=file_line.readline()[:-1]
        data=line.split()
        if len(data)==2:
            liste_tous_sommets.append(data[0])
            liste_tous_sommets.append(data[1])
        i=i+1
    dict_prot_degre={}
    for sommet in liste_tous_sommets:
        if sommet not in dict_prot_degre:
            dict_prot_degre[sommet]=1
        else:
            dict_prot_degre[sommet]=dict_prot_degre[sommet]+1
    int_somme_deg=sum(dict_prot_degre.values())
    int_nombre_sommet=len(dict_prot_degre.keys())
    print("Le dictionnaire est :",dict_prot_degre)
    doub_degre_moy=int_somme_deg/int_nombre_sommet
    print("somme des degres des proteines du graphe est :",int_somme_deg)
    print("nombre de proteines du graphe est : ", int_nombre_sommet)
    print("le degré moyen des protéines du graphe est :")
    file_line.close()
    return doub_degre_moy
print(get_ave_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_examplev1.txt"))

##Fonction calculer le nombre de protéines du graphe dont le degré est exactement égal à deg
def count_degree(file, deg):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    #nombre_arretes=0
    liste_tous_sommets=[]
    i=0
    while i<number_line:
        line=file_line.readline()[:-1]
        data=line.split()
        if len(data)==2:
            liste_tous_sommets.append(data[0])
            liste_tous_sommets.append(data[1])
        i=i+1
    dict_prot_degre={}
    for sommet in liste_tous_sommets:
        if sommet not in dict_prot_degre:
            dict_prot_degre[sommet]=1
        else:
            dict_prot_degre[sommet]=dict_prot_degre[sommet]+1
    #dictionnaire qui contient les protéines et leur dégré
    print("Le dictionnaire est ",dict_prot_degre)
    str_prot_de_deg=''
    int_count=0
    for prot in dict_prot_degre:
        if dict_prot_degre[prot]==deg:
            int_count=int_count+1
            str_prot_de_deg=str_prot_de_deg+','+prot
    int_nombre_prot=int_count
    file_line.close()
    print("le nombre de proteine(s) qui a(ont) degre =",deg, "est : ")
    return(int_nombre_prot,deg)
print(count_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_v2.txt",1))
##le nombre de protéines ayant un degré d(compris entre dmin et dmax)
def histogram_degree(file, dmin, dmax):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    #nombre_arretes=0
    liste_tous_sommets=[]
    i=0
    while i<number_line:
        line=file_line.readline()[:-1]
        data=line.split()
        if len(data)==2:
            liste_tous_sommets.append(data[0])
            liste_tous_sommets.append(data[1])
        i=i+1
    print(liste_tous_sommets)
    dict_prot_degre={}
    for sommet in liste_tous_sommets:
        if sommet not in dict_prot_degre:
            dict_prot_degre[sommet]=1
        else:
            dict_prot_degre[sommet]=dict_prot_degre[sommet]+1
    #dictionnaire qui contient les protéines et leur dégré
    print("Le dictionnaire est ",dict_prot_degre)
    int_count=0
    for prot in dict_prot_degre:
        if (dict_prot_degre[prot]>= dmin and dict_prot_degre[prot]<= dmax):
            int_count=int_count+1
    
    deg=1
    for sommet in dict_prot_degre:
        ligne_hist=str(deg)+""
        if (dict_prot_degre[sommet]>= dmin and dict_prot_degre[sommet]<= dmax):
            ligne_hist=ligne_hist+"*"
            print(ligne_hist)
        deg=deg+1
    print(ligne_hist)
    file_line.close()
    print("le nombre de proteine(s) qui a(ont) degre compris entre",dmin,"et",dmax, "est : ")
    return(int_count)
print(histogram_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_examplev1.txt",2,3))
    
