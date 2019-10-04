#affiche une suite de 12 nombres
#dont chaque terme est égale au triple
#du précédent

a,c=1,1
while c<13:
    print(a,end=" ")
    a,c=a*3,c+1
    
