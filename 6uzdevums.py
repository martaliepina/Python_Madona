"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās vērtības starpības dubultu.

"""

sk1=float(input("ievadi skaitli: "))
sk2=int(17)

starpība=sk1-sk2

if starpība > 17:print(starpība * 2)

else: print(starpība)
