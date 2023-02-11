x=int(input("donner un entier "))
f=1
for i in range(2,x+1):
    f*=i
    #f=f*i
print("la factoriel de %s est : %s" % (x,f))