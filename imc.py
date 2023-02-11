poids=float(input("donner votre poid"))
taille=float(input("donner votre taille"))
imc=round(poids/taille**2)
remarque=""
if imc<20:
    remarque="maigre"
elif imc<=25:
    remarque="idéale"
else:
    remarque="surpoids"
print("Le IMC %s est %s"%(imc,remarque))

    