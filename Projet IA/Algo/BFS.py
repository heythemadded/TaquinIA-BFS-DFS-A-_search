import copy
from Algo.Cellule import Cellule
import timeit



###Inisilisation des constante
etat_final = [[1,2,3],[8,0,4],[7,6,5]]
operation = {"H" : [-1, 0], "B" : [1, 0], "G" : [0, -1], "D" : [0, 1]}

class Taquin:
    ###Constructeur
    def __init__(self,taquin_courant,taquin_precendent):
        self.taquin_courant=taquin_courant
        self.taquin_precedent=taquin_precendent



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

### Fonction qui met les fils du noeud actuelle dans la liste queue
##input => Obj(taquin) -- queue liste de Taquin sf [Taquin,...] 
#--visited dict de Taquin sf {Str(taquin):Obj(Taquin),...}
def fils (taquin,queue,visited):
    
    pos_vid=pos_case_vide(taquin.taquin_courant)

    for op in operation :
        new_pos=Cellule(pos_vid.x+operation[op][0],pos_vid.y+operation[op][1]) 
        if 0<=new_pos.x<3 and 0<=new_pos.y<3 : ##Verifier permuation possible

            nv_taquin=copy.deepcopy(taquin.taquin_courant)
            permuter(nv_taquin,pos_vid,new_pos)
            ###Pour qu'un taquin soit ajoutée il faut qu'il ne soit pas deja visité(Non présent dans la liste visited):
            if not (str(nv_taquin) in visited.keys() ):
                queue.append(Taquin(nv_taquin,taquin.taquin_courant))

###Definition de la fonction qui donne le chemin optimal parcouru pour arriver au but
def chemin(td,visited):##input =>visited dict de Taquin sf {Str(taquin):Obj(Taquin),...}
    
    taquin= visited[str(etat_final)]
    chemin= []
    while taquin.taquin_courant!=td:
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
    queue=[Taquin(taquin,taquin)]
    visited={}

    while True:
        ##Soit queue la list des element a traiter.
        #On enleve le premier element de la liste queue pour le traiter
        tq_c=queue.pop(0)
        visited[str(tq_c.taquin_courant)]=tq_c ##Ajouter le noeud a la liste visitée

        if verif(tq_c.taquin_courant): ##Test-but
            stopt=timeit.default_timer()
            return chemin(taquin,visited),len(visited),format(stopt-startt,".8") ##Chemin ,Temps d'exe

        ##Si taquin non final on cherche ses fils et store les non visisté dans la queue
        fils(tq_c,queue,visited)
