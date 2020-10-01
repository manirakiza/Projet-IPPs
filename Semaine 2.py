#Semaine 2 : Exploration du graphe d’interactions protéine-protéine 
# Q1 Fonction pour compter compte le nombre de sommets d’un graphe.
def count_vertices(file):
    file_compte=open(file,"r") #lire un fichier 
    premier_ligne=int(file_compte.readline()[:-1]) #premier ligne correspondant au nombre de ligne du fichier 
    int_nombre_sommet=0
    liste_sommet=[]  
    for i in range(0,premier_ligne):
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
print(count_vertices("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))     

#Q2 Fonction pour compter  le nombre d’arêtes d’un graphe.
def count_edges(file):
    file_line=open(file,"r")
    number_line=int(file_line.readline()[:-1])
    int_nombre_ar=0
    liste_aretes=[]
    for line in range(0,number_line):
        line=file_line.readline()[:-1]
        if line:
            data=line.split()
            tuples=(data[0],data[1])
            liste_aretes.append(tuples)
    print(liste_aretes)
    int_nombre_ar=len(liste_aretes)
    file_line.close()
    return int_nombre_ar
print(count_edges("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))
#Fonction pour eliminer toutes les interactions redondantes et tous les homo-dimères
#Fonction qui elimine les interactions redondantes et homo-dimères
def clean_interactome(file):
    file=open(file,"r")
    number_line=int(file.readline()[:-1])
    liste=[]
    i=0
    while i<number_line:
        line=file.readline()[:-1]
        data=line.split()
        if len(data)==2:
            truples=(data[0],data[1])
            liste.append(truples)     
        i=i+1
    print(liste)
    new_liste=[]
    fo (sommet1,sommet2) in liste:
        if sommet1!=sommet2:
            new_liste.append((sommet1,sommet2))
    
        i=0
        for (sommet1,sommet2) in new_liste:
            nouveau_liste=(sommet2,sommet1)
            j=1
            for (sommet11,sommet22) in new_liste[j:]:
                if (sommet11,sommet22)==(sommet1,sommet2):
                    new_liste.remove((sommet11,sommet22))
                if (sommet11,sommet22)==nouveau_liste:
                    new_liste.remove((sommet11,sommet22))
                 j=j+1
             i=i+1
    
print(clean_interactome("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_v3.txt"))
#Fonction pour retourner le dégré maximale et le nom d'une proteine 
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
            str_prot_deg=str_prot_deg+','+prot
    file_line.close()
    print("proteine(s) qui a(ont) degre max =",int_max_deg, "est : ")
    return(str_prot_deg,int_max_deg)
print(get_max_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"))

#Fonction pour calculer le degré moyen des protéines du graphe.
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
    print("le degré moyen des protéines du graphe est :")
    file_line.close()
    return doub_degre_moy
print(get_ave_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_v2.txt"))

#Fonction calculer le nombre de protéines du graphe dont le degré est exactement égal à deg
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
#le nombre de protéines ayant un degré d(compris entre dmin et dmax)
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
    file_line.close()
    print("le nombre de proteine(s) qui a(ont) degre compris entre",dmin,"et",dmax, "est : ")
    return(int_count)
print(histogram_degree("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_v2.txt",2,3))
    


