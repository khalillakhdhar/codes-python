liste=[]
#initialisation
data =""
while(data!="0" and data!="stop" and len(liste)<=10):
    data=input("donnez une valeur")
    liste.append(data)
for i in liste:
    if i!="":
        print(i)
x,y=1,1
x=7
print(x,y)
ls=(1,2,3)
# le tuple (...) est en lecture seulement mais la liste et en lecture et écriture
print(type(ls))
print(type(liste))
print(ls)