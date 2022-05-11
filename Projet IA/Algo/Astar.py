import copy
from Algo.Cellule import Cellule
import timeit
#from Cellule import Cellule


###Inisilisation des constante
etat_final = [[1,2,3],[8,0,4],[7,6,5]]
operation = {"H" : [-1, 0], "B" : [1, 0], "G" : [0, -1], "D" : [0, 1]}

class Taquin:
    ###Constructeur
    def __init__(self,taquin_courant,taquin_precendent,g,h):
        self.g=g
        self.taquin_courant=taquin_courant
        self.taquin_precedent=taquin_precendent
        self.h=h

    ###Fonction d'evaluation f(n)=h(n)+g(n) d'un noeud
    def f(self):
        return self.h+self.g


####Fonction qui verifier si le taquin courant est final ou non (Test-but)
def verif(taquin):
    if taquin!=etat_final:
        return False
    return True

##Fonction qui permet de retourner les coordonée de la case vide
def pos_case_vide(taquin):
    for i in range(3):
        for j in range(3):
            if taquin[i][j]==0:
                c=Cellule(i,j)
                return c


def afficher_taquin(taquin):
    x="    ----------------------\n"
    for i in range(3):
        for j in range(3):
            x=x+"   |   "+str(taquin[i][j])
        x=x+"  |\n"+"    ----------------------\n"
    return x   

##Fonction qui permet le permutation entre 2 cellule 
def permuter(taquin,c1,c2):
    aux=taquin[c1.x][c1.y]
    taquin[c1.x][c1.y]=taquin[c2.x][c2.y]
    taquin[c2.x][c2.y]=aux

###Fonction qui retroune le nombre de case mal placés
def BadPlaced(taquin):
    f=[[1,2,3],[8,0,4],[7,6,5]]
    h=0
    for i in range(3):
        for j in range(3):
            if taquin[i][j]!=0 and taquin[i][j]!=f[i][j]:
                h=h+1
    return h
    
### Fonction qui met les fils du noeud actuelle dans la liste queue 
def fils (taquin,queue,visited):##input => Obj(taquin) -- queue,visited dictionnaire sf {str(taquin):Obj(taquin),...}
    pos_vid=pos_case_vide(taquin.taquin_courant)

    for op in operation :
        new_pos=Cellule(pos_vid.x+operation[op][0],pos_vid.y+operation[op][1]) 
        if 0<=new_pos.x<3 and 0<=new_pos.y<3 : ##Verifier permuation possible

            nv_taquin=copy.deepcopy(taquin.taquin_courant)
            permuter(nv_taquin,pos_vid,new_pos)
            g,h=taquin.g+1,BadPlaced(nv_taquin)
            ###Pour qu'un taquin soit ajoutée il faut qu'il verifie qlq condiotion:
                ##1/N'est pas deja visité(Non présent dans la liste visited)
                ##2/N'existe pas le même taquin avec un f(n) inferieur au nv_taquin dans queue
            if not (str(nv_taquin) in visited.keys() or str(nv_taquin) in queue.keys() and queue[str(nv_taquin)].f() <h+g ):
                queue[str(nv_taquin)]=Taquin(nv_taquin,taquin.taquin_courant,g,h)

###Fonction qui permet de choisir le meilleur taquin a explorés
def meilleur_taquin(queue) :##input => queue Dictionnaire{str(taquin):Obj(taquin),...}

    premiere_it=True
    for tq in queue.values():
        if premiere_it or tq.f() < Mtq.f() :
            premiere_it=False
            Mtq=tq
    return Mtq

###Definition de la fonction qui donne le chemin optimal parcouru pour arriver au but
def chemin(visited):##input =>Dict sf {str(taquin):Obj(Taquin)}
    
    taquin= visited[str(etat_final)]
    chemin= []
    while taquin.g !=0:
        chemin.append(
            {"TAQUIN":taquin.taquin_courant}
        )
        taquin=visited[str(taquin.taquin_precedent)]
    chemin.append({"Initiale":taquin.taquin_courant})
    chemin.reverse()
    return chemin


def main (taquin):

    startt=timeit.default_timer()
        ###Inisialisation de Queue 
    queue={str(taquin):Taquin(taquin,taquin,0,BadPlaced(taquin))}
    visited={}

    while True:
        tq_c=meilleur_taquin(queue)##Rechercher le meilleur taquin disponible
        visited[str(tq_c.taquin_courant)]=tq_c ##Ajouter le noeud a la liste visitée

        if verif(tq_c.taquin_courant ): ##Test-but
            stopt=timeit.default_timer()
            return chemin(visited),len(visited),format(stopt-startt,".8") ##Chemin ,Temps d'exe

        ##Si taquin non final on cherche ses fils et store les non visisté dans la queue
        fils(tq_c,queue,visited)
        ##On efface le noeud deja visitée pour ne pas retournée en arriere
        del queue[str(tq_c.taquin_courant)]
        
#print(main([[3,2,7],[8, 6, 0],[1, 5, 4]]))



