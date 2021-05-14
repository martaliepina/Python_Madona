"""
    Funkcija akrs akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to kubu starpību un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, ievadot nepieciešamās
    vērtības un parādot skaitli ar pieciem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu kubu starpību
"""
def akrs (viens,divi,trīs):
    summa=viens**3+divi**3+trīs**3
    return summa

pirmais=int(input("ievadi pirmo skaitli: "))
otrais=int(input("ievadi otro skaitli: "))
trešais=int(input("ievadi trešo skaitli: "))

maijs=akrs(pirmais,otrais,trešais)

print("{0:.5f}".format(maijs))