sb=int(input("donnez la salaire brute "))
taxe=0
if sb<800:
    taxe=sb*0.05
elif sb<1700:
    taxe=sb*0.12
else:
    taxe=sb*0.15
net=sb-taxe
print("la salaire brute %s a comme taxe la valeur: %s et le montant net à recevoir est de : %s"%(sb,taxe,net))

    
