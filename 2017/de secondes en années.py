 #programme qui convertit un nombre entier de secondes
 #fourni au départ en un nombre
 #d'années, de mois, de jours, de minutes et de secondes (avec utilisation
 #de l'opérateur modulo)

#le nombre de secondes est fourni au départ:
nsd=12345678912

#nombre de secondes dans une journée
nspj=3600*24

#nombre de secondes dans un an (365jours)
#on ne tiendra pas compte des années bisextiles

nspa=nspj*365

#nombre de secondes dans un mois en admettant
#pour chaque mois une durée identique de 30jours

nspm=nspj*30

#Nombre d'années contenues dans la durée fournie :
na = nsd // nspa    # division <entière>
nsr = nsd % nspa    # n. de sec. restantes 
# Nombre de mois restants :
nmo = nsr // nspm    # division <entière> 
nsr = nsr % nspm    # n. de sec. restantes 

# Nombre de jours restants : 
nj = nsr // nspj    # division <entière> 
nsr = nsr % nspj    # n. de sec. restantes 
# Nombre d'heures restantes : 
nh = nsr // 3600    # division <entière> 
nsr = nsr % 3600    # n. de sec. restantes 
# Nombre de minutes restantes : 
nmi = nsr // 60     # division <entière> 
nsr = nsr % 60	      # n. de sec. restantes 
 
print("Nombre de secondes à convertir :", nsd) 
print("Cette durée correspond à", na, "années de 365 jours, plus") 
print(nmo, "mois de 30 jours,", end=' ') 
print(nj, "jours,", end=' ') 
print(nh, "heures,", end=' ') 
print(nmi, "minutes et", end=' ') 
print(nsr, "secondes.")
