#recherche d'un caractère particulier dans une chaine

#chaine fournie au départ:
ch="Monty python flying circus"

#caractère à rechercher:
cr="e"

#recherche proprement dite:
lc=len(ch)    #nombre de caractère à tester
i=0     #indice du caracère en cours d'examen
t=0     #"drapeau" à lever si le caractère recherché est présent

while i<lc:
    if ch[i]==cr:
        t=1
    i=i+1
    #affichage:
print("Le caractère",cr,end=" ")
if t==1:
    print("est présent",end=" ")
else:
    print("est introuvable",end=" ")
print("dans la chaine",ch)

