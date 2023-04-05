import sqlite3

with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    
#Les données de la dépense
def depense_total():
    print("Remplissez la liste de vos dépense:")
loyer = int(input("Donnez le montant du loyer:"))
Manger = int(input("Le bilan du mangé:"))
Transport = int(input("Donnez la somme des tarifs du transprt:"))
Loisir = int(input("Donnez la somme effectuée du Loisir:"))
Tontine = int(input("La somme versée de la Tontine:"))
Factures_courant = int(input("Donnez la somme des factures:"))
requete ="INSERT INTO depense_total('loyer', 'Manger', 'Transport', 'Loisir', 'Tontine', 'Factures_courant') VALUES (?,?,?,?,?,?)"
cursor.execute(requete, (loyer, Manger, Transport, Loisir, Tontine, Factures_courant))
connection.commit() 
depense_total()
       
#La somme totale de la depense
depense_totale = loyer+Manger+Transport+Loisir+Tontine+Factures_courant
print("la somme dépensé" +str(depense_totale)+ "Franc(CFA)")
if depense_totale > 1000000:
    print("Votre dépense est hyper élevé")
else:
    print("vous avez bien géré vos dépense")
    
connection.commit()

#Les données du revenu
def revenu_total():
    print("Remplissez la liste de vos dépense:")
Salaire = int(input("La somme de votre salaire:"))
Business = int(input("la somme gagnée du business:"))
tontine = int(input("La somme gagnée à la tontine:"))
requete ="INSERT INTO budget('Salaire', 'Business', 'tontine') VALUES(?,?,?)"
cursor.execute(requete,(Salaire, Business, tontine))
connection.commit()
    
#La somme totale des revenus
revenu_totale = Salaire+Business+tontine
print("La somme des revenus" +str(revenu_totale)+ "Franc(CFA)")
if revenu_totale > 500000:
    print("Vous pouvez souffler")
else:
    print("vous avez pratiquement rien gagner")
    
connection.commit()

#La différence qui existe entre la depense et le revenu
La_difference = revenu_totale - depense_totale
print("Donnez la difference effectuée:")
if revenu_totale > depense_totale:
    print("Vous avez bien géré vos transactions")
elif revenu_totale < depense_totale:
    print("vous n'avez pas bien géré vos transactions")
else:
    print("On a un égalité de somme entre les deux")
    
connection.commit()

connection.close()