# Inversion d'une chaîne de caractères
 
# Chaîne fournie au départ :
ch = "zorglub"
lc = len(ch)	 # nombre de caractères total
i = lc - 1     # le traitement commencera à partir du dernier caractère
nch = ""     # nouvelle chaîne à construire (vide au départ)
while i >= 0:
  nch = nch + ch[i]
  i = i - 1
# Affichage :
print(nch)
