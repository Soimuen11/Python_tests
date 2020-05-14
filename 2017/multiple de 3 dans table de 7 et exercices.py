# affichage des 20 premiers termes de la table par 7,
# avec signalement des multiples de 3 :
 
i = 1		# compteur : prendra successivement les valeurs de 1 à 20
while i < 21:
  # calcul du terme à afficher :
  t = i * 7
  # affichage sans saut à la ligne (utilisation de la virgule) :
  print(t, end =" ")
  # ce terme est-il un multiple de 3 ? (utilisation de l'opérateur modulo) :
  if t % 3 == 0:
      print("*", end =" ")    #affichage d'une astérisque dans ce cas
  i = i + 1		# incrémentation du compteur dans tous les cas


print("====================================================")

a,b,c,d,e="*","**","***","****","*****"
print(a,b,c,d,e)
print(a)
print(b)
print(c)
print(d)
print(e)

print("====================================================")

a, b, c = 1, 1, 1
while c <50:
     print(c, ":", b, type(b))
     a, b, c = b, a+b, c+1

print("====================================================")

a,b,c=3,2,1
while c<15:
    print(c, ":",b)
    a,b,c=b,a*b,c+1
