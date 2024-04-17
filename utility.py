#le funzioni devo essere messe in capo al programma
#crea funzione
#scrivi elementi dizionario
def stampaDizionario(diz):
    for key, value in diz.items():
        print("la chiave è: "+key)
        print("il valore è: "+str(value))

#calcola il totale delle ore del dizionario
def oreTotali(diz):    
    oreTOT=0
    for key, value in dizionario.items():
        oreTOT+=value
    return oreTOT

#numero degli insegnanti con cattedra piena
def cattedrePiene(diz):
    contaInsegnanti=0
    for key, value in diz.items():
        if value==18:
            contaInsegnanti+=1
    return contaInsegnanti

#funzione che modifichi le ore allocate ad un insegnante
def cambiaOreInsegnante(diz, insegnante, ore):
    if insegnante in diz:
        diz[insegnante]=ore

def scalaMonteOre(diz, insegnante, oreDaRimuovere):
    if insegnante in diz:
        oreAttuali=diz[insegnante]
        if oreAttuali>=oreDaRimuovere:
            diz[insegnante]=oreAttuali-oreDaRimuovere

#creare dizionari
#{"KEY":valore}
dizionario={"rossi":18,"bianchi":16,"verdi":6}
#aggiungere una coppia dentro il dizionario
dizionario["viola"]=14
#scrivere il dizionario
print(dizionario)
#modificare una coppia chiave valore
dizionario["bianchi"]=18
print(dizionario)

#richiamiamo un metodo
stampaDizionario(dizionario)
print("ore totali: ", oreTotali(dizionario))
print("insegnanti con cattedra piena: ", cattedrePiene(dizionario))
cambiaOreInsegnante(dizionario, "peschi", 6)
scalaMonteOre(dizionario, "bianchi", 18)
print(dizionario)
