a=int(input("donner un entier"))
b=int(input("donner un entier"))
x=a
y=b
while a!=b:
    if(a>b):
        a=a-b
    else:
        b=b-a
print("le pgcd de %s et %s est: %s"%(x,y,a))