class Interactome:
    def __init__(self,file):
        self.file=file
        self.int_list=self.read_interaction_file_list(file)
        self.int_dict=self.read_interaction_file_dict(file)
        self.proteins=list(self. nom_dict.keys())
    
    def read_interaction_file_dict(self):
        self.file_line=open(self.file,"r")
        nbre_ligne=int(self.file_line.readline()[:-1])
        nom_dict={}
        line=0
        while line<nbre_ligne:
            ligne = self.file_line.readline()[:-1]
            data = ligne.split()
            sommet_graphe1 = data[0]
            sommet_graphe2= data[1]
            if not(sommet_graphe1 in nom_dict):
                nom_dict[sommet_graphe1] = []
                nom_dict[sommet_graphe1].append(sommet_graphe2)
            line +=1
        self.file_line.close()  
        return nom_dict
    
    def read_interaction_file_list(self):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
        list_sommet=[]
        for line in range(0,number_line):
            line=self.file_line.readline()[:-1]
            if line:
                data=line.split()
                sommet_graphe1=data[0]
                sommet_graphe2=data[1]
                tuples=(sommet_graphe1,sommet_graphe2)
                list_sommet.append(tuples)
        self.file_line.close()
        return list_sommet
    def read_interaction_file(self,file):
        d_int=self.read_interaction_file_dict(file)
        l_int=self.read_interaction_file_list(file)
        return(d_int,l_int)
    
    def is_interaction_file(self):
        self.file_test=open(self.file,"r")
        line_number=int(self.file_test.readline()[:-1]) #première ligne du fichier correspondant au nbre de ligne nombre_ligne=0
        val=0
        while val < line_number:
            line_inter=self.file_test.readline()[:-1]
            data=line_inter.split()
            if len(data)==2:
                nombre_ligne =nombre_ligne+1
            val +=1
            print(nombre_ligne)
            str_reponse=""
            if nombre_ligne!= line_number:
                str_reponse='false'
                #print(str_reponse)
            elif len(data)>2 or len(data)<2:
                str_reponse='false'
        #print(str_reponse)
            else:
                str_reponse='true'
        self.file_test.close()
        return str_reponse
    
    def count_vertices(self):
        self.file_compte=open(self.file,"r") #lire un fichier
        premier_ligne=int(self.file_compte.readline()[:-1]) #premier ligne correspondant au nombre d'interaction de fichier
        int_nombre_sommet=0
        liste_sommet=[]
        i=0
        while i< premier_ligne:
            sommet_arret=self.file_compte.readline()[:-1]
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
        self.file_compte.close()
        return int_nombre_sommet
    def count_edges(self):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
        int_nombre_ar=0
        liste_aretes=[]
        j=0
        while j<number_line:
            line=self.file_line.readline()[:-1]
            if line:
                data=line.split()
                tuples=(data[0],data[1])
                liste_aretes.append(tuples)
            j=j+1
        print(liste_aretes)
        int_nombre_ar=len(liste_aretes)
        self.file_line.close()
        return int_nombre_ar
    
    def clean_interactome(self):
        self.outfile=open(("D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example_clean.txt"),"w")
        self.file=open(self.file,"r")
        number_line=int(self.file.readline()[:-1])
        liste=[]
        i=0
        while i<number_line:
            line=self.file.readline()[:-1]
            data=line.split()
            if len(data)==2:
                truples=(data[0],data[1])
                liste.append(truples)
            i=i+1
        print(liste)
        nouveau_liste=[]
        for sommet in liste:
            if sommet[0]!=sommet[1]:
                nouveau_liste.append(sommet) #liste d'interactions sans homo-dimères
        for sommet_inv in nouveau_liste:
            somet_list_inver=(sommet_inv[1],sommet_inv[0])
            i=1
            for sommet_suivant in nouveau_liste[i:]:
                if sommet_suivant[0]==sommet_inv[1] and sommet_suivant[1]==sommet_inv[0]:
                    nouveau_liste.remove(sommet_suivant)
                    if sommet_suivant[0]==somet_list_inver[1] and sommet_suivant[1]==somet_list_inver[0]:
                        nouveau_liste.remove(sommet_suivant)
                i=i+1
            for interaction in nouveau_liste:
                self.outfile.write(str(interaction[0]+" "+interaction[1]+"\n"))
        self.file.close()
        self.outfile.close()
    
    def get_degree(self, prot):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
    #nombre_arretes=0
        liste_tous_sommets=[]
        i=0
        while i<number_line:
            line=self.file_line.readline()[:-1]
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
        str_prot_de_deg=''
        int_deg=0
        for protein in dict_prot_degre.keys():
            if protein==prot:
                int_deg=int_deg+dict_prot_degre[protein]
                str_prot_de_deg=protein
        self.file_line.close()
        return(str_prot_de_deg,int_deg)
    
    def get_max_degree(self):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
    #nombre_arretes=0
        liste_tous_sommets=[]
        i=0
        while i<number_line:
            line=self.file_line.readline()[:-1]
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
        str_prot_deg=''
        int_max_deg=max(dict_prot_degre.values())
        for prot in dict_prot_degre:
            if dict_prot_degre[prot]==int_max_deg:
                str_prot_deg=str_prot_deg+' '+prot
        self.file_line.close()
        return(str_prot_deg,int_max_deg)
    
    ##Fonction pour calculer le degré moyen des protéines du graphe.
    def get_ave_degree(self):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
    #nombre_arretes=0
        liste_tous_sommets=[]
        i=0
        while i<number_line:
            line=self.file_line.readline()[:-1]
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
        doub_degre_moy=int_somme_deg/int_nombre_sommet
        self.file_line.close()
        return doub_degre_moy
  ##Fonction calculer le nombre de protéines du graphe dont le degré est exactement égal à deg
    def count_degree(self, deg):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
    #nombre_arretes=0
        liste_tous_sommets=[]
        i=0
        while i<number_line:
            line=self.file_line.readline()[:-1]
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
        str_prot_de_deg=''
        int_count=0
        for prot in dict_prot_degre:
            if dict_prot_degre[prot]==deg:
                int_count=int_count+1
                str_prot_de_deg=str_prot_de_deg+','+prot
        int_nombre_prot=int_count
        self.file_line.close()
        return(int_nombre_prot,self.deg)

    def histogram_degree(self, dmin, dmax):
        self.file_line=open(self.file,"r")
        number_line=int(self.file_line.readline()[:-1])
    #nombre_arretes=0
        liste_tous_sommets=[]
        i=0
        while i<number_line:
            line=self.file_line.readline()[:-1]
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
            int_count=0
            for prot in dict_prot_degre:
                if (dict_prot_degre[prot]>= dmin and dict_prot_degre[prot]<= dmax):
                    int_count=int_count+1
        deg=1
        for sommet in dict_prot_degre:
            ligne_hist=str(deg)+""
            if (dict_prot_degre[sommet]>= dmin and dict_prot_degre[sommet]<= dmax):
                ligne_hist=ligne_hist+"*"
            deg=deg+1
        self.file_line.close()
        return(int_count)
    if __name__ == " __main__ ":
        file="D:/M2 2020-2021/Reseaux Biologiques Projet/toy_example.txt"
        fich=Interactome(file)
        test_deg=fich.get_degree(file)
    
