x=int(input("donner la valeur inferieur"))
y=int(input("donner la valeur supérieur"))
s=0
for i in range(x,y+1):
    s+=i
    if i%3==0:
        print(i)
print("la somme des éléments entre %s et %s est: %s"%(x,y,s))