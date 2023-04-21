import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    

class Gestion_Contact:
    
    def __init__(self, montant):
        self.solde_compte=montant
        print("votre compte est de:", montant)

        
    def le_revenu(self):
        somme_obtenu=float(input("donnez la somme obtenu:"))
        print(somme_obtenu)
        self.solde_compte=self.solde_compte+somme_obtenu
        return self.solde_compte
    
    def la_depense(self): 
        somme_dépensé=float(input("donnez la somme dépensé:"))
        print(somme_dépensé) 
        if self.solde_compte>somme_dépensé:
             self.solde_compte=self.solde_compte-somme_dépensé
             return self.solde_compte
        else:
             print("votre solde est insuffissant")
             
    def affichageinfo(self):
        print("l'ecart qui existe entre les deux est:",self.solde_compte)
        
compte=Gestion_Contact(25000)
compte.le_revenu()
compte.la_depense()
compte.affichageinfo()