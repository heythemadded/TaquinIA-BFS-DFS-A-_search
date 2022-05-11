import tkinter.font as tkFont
import tkinter as tk
from Algo import Astar,BFS,DFS,DFSL
from random import shuffle

global n, branche_solution, etapes_solution, Nbr_total_noeuds_explores, temps
##Inisialisation de taquin par shuffle
def init_taquin():
    global etat_depart
    L = list(i for j in etat_depart for i in j)
    shuffle(L)
    etat_depart= [[L[0],L[1],L[2]],[L[3],L[4],L[5]],[L[6],L[7],L[8]]]
    for i in range(9) :
        ListeT = list(i for j in etat_depart for i in j)
        ligne, col = i // 3, i % 3
        can.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

##Afficher le noeud suivant:
def noeud_suivant():
    global n
    n+=1
    for i in range(9) :
        if n>etapes_solution:
            break
        else:
            ListeT = list(i for j in branche_solution[n]['TAQUIN'] for i in j)
            ligne, col = i // 3, i % 3
            can2.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])


##Permet de resoudre le taquin selon l'algorithm choisit et
##Ouvre une autre fenetre affichant les données de de realisation de l'algorithme    

def solve(algo):
    global branche_solution, etapes_solution, img, can2, texte, n, Nbr_total_noeuds_explores,algorith
    n=0
    algorith=algo
    if algo=='Astar':
        branche_solution, Nbr_total_noeuds_explores, temps = Astar.main(etat_depart)
    elif algo=='BFS':
        branche_solution, Nbr_total_noeuds_explores, temps = BFS.main(etat_depart)
    elif algo=='DFS':
        Nbr_total_noeuds_explores, temps,branche_solution=DFS.main(etat_depart)
    elif algo=='DFSL':
        Nbr_total_noeuds_explores, temps,branche_solution=DFSL.main(etat_depart)

    etapes_solution = len(branche_solution) - 1

    # Interface graphique
    root.destroy()
    # créer la fenetre
    Window = tk.Tk()
    Window['bg'] = 'white'
    Window.title('IA - Algo ')
    Window.geometry("540x600-400-150")

    tk.Label(text="L'algorithme choisit est: {}".format(algo),bg='white',width=70,height=5,font=("Arial",10,"bold")).pack()

    # créer une zone Canvas destinée à placer les images des cases
    can2 = tk.Canvas(height=380, width=380, bg='#328fa8')
    can2.pack()

    # importer les images 
    img = []
    for i in range(9) :
        img.append(tk.PhotoImage(file="Images/" + str(i) + ".png"))

    #Noeud && noeud_suivant

    tk.Label(text="Total des nœuds explorés(Noeuds initial inclus) : {} noeuds\nCoût du chemin-solution(steps): {}\nTemps d'exécution: {}".format(
                     Nbr_total_noeuds_explores,etapes_solution, temps),bg='white',width=70,height=5,font=("Arial",10,"bold")).pack()

    tk.Button(text='Nœud suivant', font=("Arial", 11), fg='black',bg='white', relief=tk.RAISED,
              command=noeud_suivant).pack()

    for i in range(9) :
        ListeT = list(i for j in branche_solution[0]['Initiale'] for i in j)
        ligne, col = i // 3, i % 3
        can2.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

    Window.mainloop()
    # FIN fenetre

####Definition des commande de chaque btn

def ActionBtn_BFS():
    solve('BFS')

def ActionBtn_DFS():
    solve('DFS')

def ActionBtn_DFSlim():
    solve('DFSL')

def ActionBtn_Astar():
    solve('Astar')


##Creation de l'interface graphique (main)
root=tk.Tk()
root.title("Projet-IA")

##Creation d'icone
img = tk.PhotoImage(file='images/taquin.jpg')
root.tk.call('wm', 'iconphoto', root._w, img)

##Definir la taille de la fenetre
root.geometry("800x600")
root.resizable(width=False, height=False)

###Definier les fonts
ft = tkFont.Font(family='Trebuchet MS',size=26)
ver = tkFont.Font(family='Verdana',size=11,weight="bold")

###Header 
Header=tk.LabelFrame(root,bg="white")
Header.place(x=0,y=0,width=801,height=121)
titre=tk.Label(Header,text="Jeu de taquin",font=ft,bg="white",justify="center")
titre.place(x=200, y=30, width=361, height=51)

###Main 
main=tk.LabelFrame(root,bg="#328fa8").place(x=0, y=120, width=801, height=481)

###Buttons 
Btn_BFS=tk.Button(main,text="BFS",justify="center",command=ActionBtn_BFS,font=ver).place(x=30, y=170, width=161, height=41)
Btn_DFS=tk.Button(main,text="DFS",justify="center",font=ver,command=ActionBtn_DFS).place(x=30, y=230, width=161, height=41)
Btn_DFS_lim=tk.Button(main,text="DFS lim",justify="center",font=ver,command=ActionBtn_DFSlim).place(x=30, y=290, width=161, height=41)
Btn_Astar=tk.Button(main,text="A*",justify="center",font=ver,command=ActionBtn_Astar).place(x=30, y=350, width=161, height=41)
Btn_Nv=tk.Button(main,text="Initialisation",font=ver,justify="center",command=init_taquin).place(x=30, y=460, width=161, height=41)

## Preparation du canva pour placer les imgs
can=tk.Canvas(height=380, width=380, bg='#328fa8')
can.place(x=320, y=140)

##Inisialization des imgs
img=[]
for i in range(9):
        img.append(tk.PhotoImage(file="Images/"+str(i)+".png"))

etat_depart= [[3,2,7],[8, 6, 0],[1, 5, 4]]
for i in range(9) :
    ListeT = list(i for j in etat_depart for i in j)
    ligne, col = i // 3, i % 3
    can.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

root.mainloop()
