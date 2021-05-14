"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""

from math import pi

pamatar=float(input("pamatar: "))
augstums=float(input("augstums: "))

laukums=(pamatar * augstums * pi * 2)

print(laukums)