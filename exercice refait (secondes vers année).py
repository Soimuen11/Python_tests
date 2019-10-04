nsd=12345678912  #nombre de secondes au départ

nspj=3600*24   #nombre de secondes dans ue journée
nspa=nspj*365  #nombre de secondes dans une année
nspm=nspj*30    #nombre de secondes dans un mois

na=nsd//nspa   #nombre de secondes de départ (nsd) contenues dans un an
nsr=nsd%nspa   #combien de secondes il reste

nm=nsr//nspm  #combien de mois tiennent dans nsr
nsr=nsr%nspm   #nombre de secondes restantes après le calcul

nj=nsr//nspj #combien de jours tiennent dans nsr
nsr=nsr%nspj  #nb de secondes restantes après calcul

nh=nsr//3600  #et enfin le nombre d'heures restantes
nsr=nsr%3600

nmin=nsr//60
nsr=nsr%60    #et le nombre de minutes

print("nombre de secondes à convertir",nsd)
print("cette durée correspond à",na,"année de 365 jours")
print(nm,"mois de 30 jours")
print(nj,"jours")
print(nh,"heures")
print(nmin,"minutes")

#je veux qu'il m'affiche le nombre de secondes de départ
#et qu'il me dise à combien d'années, de mois, de jours et de minutes,
#nsd correspond.




