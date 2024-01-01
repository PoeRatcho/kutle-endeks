print("KÜTLE ENDEKS HESAPLAMA PROGRAMI")
boy = float(input("Boy(Cm): "))
kilo = float(input("Kilo: "))
vki = (kilo / (boy * boy))
print(vki)

if vki == 18 or vki <= 25:
    print("Normal")
elif vki == 26 or vki <= 30:
    print("Kilolu")
elif vki == 31 or vki <= 35:
    print("Obez")
else:
    print("Çok Obez Kilo Vermelisin")