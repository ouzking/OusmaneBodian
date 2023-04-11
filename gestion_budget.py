import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    
cursor.execute(
    "CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY AUTOINCREMENT,loyer TEXT, Manger TEXT, Transport TEXT, Loisir TEXT, Tontine TEXT, Factures_courant TEXT, Salaire TEXT, Business TEXT, tontine TEXT)")

class GestionBudget:
    
    
    def __init__(self):
        print("l'application de gestion de budget")


    def depense_total(self):
        print("Remplissez la liste de vos dépense:")
        loyer = int(input("Donnez le montant du loyer:"))
        Manger = int(input("Le bilan du mangé:"))
        Transport = int(input("Donnez la somme des tarifs du transprt:"))
        Loisir = int(input("Donnez la somme effectuée du Loisir:"))
        Tontine = int(input("La somme versée de la Tontine:"))
        Factures_courant = int(input("Donnez la somme des factures:"))
        cursor.execute("INSERT INTO depense('loyer', 'Manger', 'Transport', 'Loisir', 'Tontine', 'Factures_courant') VALUES (?,?,?,?,?,?)",(loyer, Manger, Transport, Loisir, Tontine, Factures_courant))
        connection.commit()
        print("les dépenses sont ajoutées")
        depense_totale = loyer+Manger+Transport+Loisir+Tontine+Factures_courant
        print("la somme dépensé" +str(depense_totale)+ "Franc(CFA)")
        if depense_totale > 1000000:
            print("Votre dépense est hyper élevé")
        else:
            print("vous avez bien géré vos dépense")
            
    def revenu_total(self):
        print("Remplissez la liste de vos dépense:")
        Salaire = int(input("La somme de votre salaire:"))
        Business = int(input("la somme gagnée du business:"))
        tontine = int(input("La somme gagnée à la tontine:"))
        cursor.execute("INSERT INTO budget('Salaire', 'Business', 'tontine') VALUES(?,?,?)",(Salaire, Business, tontine))
        connection.commit()
        print("vos revenus ont été consulté")
        revenu_totale = Salaire+Business+tontine
        print("La somme des revenus" +str(revenu_totale)+ "Franc(CFA)")
        if revenu_totale > 500000:
            print("Vous pouvez souffler")
        else:
            print("vous avez pratiquement rien gagner")
            
    def difference(self):
        depense_totale = ("loyer+Manger+Transport+Loisir+Tontine+Factures_courant")
        revenu_totale = ("Salaire+Business+tontine")
        self.La_difference = revenu_totale - depense_totale
        print("Donnez la difference effectuée:")
        if revenu_totale > depense_totale:
            print("Vous avez bien géré vos transactions")
        elif revenu_totale < depense_totale:
            print("vous n'avez pas bien géré vos transactions")
        else:
            print("On a un égalité de somme entre les deux")
            
    def le_tarif_des_budgets(self):
        choix =""
        print("       Bonjour comment vous allez ?      ")
        print("                                         ")
        print("   A) Remplissez vos dépenses")
        print("   B) Consultez vos revenus")
        print("   C) Vérifier la difference entre la dépense et le revenu")
        print("   0) quitter l'application")
        choix = input("quel est votre désire:\n")
        if choix == "A":
            self.depense_total()
            self.le_tarif_des_budgets()
        elif choix == "B":
            self.revenu_total()
            self.le_tarif_des_budgets()
        elif choix == "C":
            self.La_difference()
            self.le_tarif_des_budgets()
        elif choix == "0":
            print("Quitter")
            exit()
        else:
            print("votre choix n'est pas reconnu" )
            

geestion_budget = GestionBudget()
geestion_budget.le_tarif_des_budgets()