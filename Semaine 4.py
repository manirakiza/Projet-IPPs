def countCC(file):
    fichier=open(file,"r")
    int_ligne=int(fichier.readline()[:-1])
    nom_dict={}
    i=0
    while i<int_ligne:
        ligne = fichier.readline()[:-1]
        data = ligne.split()
        if len(data)!=0:
            if not(data[0] in nom_dict):
                nom_dict[data[0]] = []
                nom_dict[data[0]].append(data[1])
        i +=1
    print(nom_dict)
    list_prot=list(nom_dict.keys())
    print(list_prot)
    comp_conn={}
    comp_pred=1
    j=0
    while j<len(list_prot):
        comp_conn[comp_pred]=[list_prot[0]]
        for prot in comp_conn[comp_pred] :
            for prot1 in nom_dict[prot]:
                    if (prot1 not in comp_conn[comp_pred]) & (prot1 in list_prot):
                        comp_conn[comp_pred].append(prot1)
            if (prot in list_prot):
               list_prot.remove(prot)
        comp_pred=comp_pred+1
        j=j+1
    print(list(comp_conn))
    for comp in comp_conn:
        comp_conn[comp]=(len(comp_conn.keys()),comp_conn[comp])
    print("on a ",len(comp_conn.keys()),"composante connexes")
    fichier.close()
    return comp_conn
print(countCC("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt"))

def writeCC(self):
    liste_cc=self.countCC()
    fichier_sortie=open("D:/M2 2020-2021/Reseaux Biologiques Projet/comp_conn.txt","w")
    for comp in liste_cc:
        print(comp)
        fichier_sortie.write(str(liste_cc[comp][0]) + " " + str(liste_cc[comp][1]) + "\n")
    fichier_sortie.close()
print(writeCC("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt"))

def extractCC(self,prot):
    dico_conv=list(self.countCC())
    list_conv=[]
    for conn in dico_conv:
        if prot in  dico_conv[conn]:
            list_conv=dico_conv[conn]
    return list_conv 
print(extractCC("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt",prot1))

def computeCC(self):
    list_cc=self.writeCC()
    indice_ccprot_list=[]
    for comp in list_cc:
        for k in comp[2]:
            if k in comp[2]:
                numerp_cc=comp[2]
                indice_ccprot_list.append(numerp_cc[1])
    return indice_ccprot_list
print(computeCC("D:/M2 2020-2021/Reseaux Biologiques Projet/semaine4.txt"))
def density(self):
    densite=(2*self.count_edges())/((len(self.get_vertices())*(len(self.get_vertices())-1)))
    return densite

def clustering(self,prot):
    int_deg_prot=self.get_degree(prot)
    coeff_clust=0
    if int_deg_prot >1:
        int_connect=0
        for som_voisin in self.nom_dict[prot]:
            for som_voisin2 in self.nom_dict[som_voisin ]:
                if som_voisin2 in self.nom_dict[prot]:
                    int_connect=int_connect+1
            coeff_clust=int_connect/(int_deg_prot*(int_deg_prot-1))
    return coeff_clust
            
    