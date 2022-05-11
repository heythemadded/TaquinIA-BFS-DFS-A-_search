
class Cellule:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def affiche_cellule(self):
        print("("+str(self.x)+","+str(self.y)+")")
