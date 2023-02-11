x=int(input("donner un entier de 3 chiffres"))
c=x//100
d=((x%100)//10)
u=x%10
somme=u+d+c
if somme % 3==0:
    print("%s est divisible par %s"%(x,3))