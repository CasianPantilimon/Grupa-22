# vizibila prima si ultima litera
# daca se repeta vor fi si ele vizizbile
# restul ascunse prin "_"
# avem 7 vieti

cuvant = "onomatopee".lower()  # o_o___o_ee
cuvant_de_ghicit = list(cuvant)
for index, valoare in enumerate(cuvant):
    # print(index, valoare)
    if cuvant[0] != valoare and cuvant[-1] != valoare:
        cuvant_de_ghicit[index] = "_"

cuvant_de_ghicit = " ".join(cuvant_de_ghicit)
print(cuvant_de_ghicit)

numar_vieti = 7
# oferim utilizatorului posibilitatea de a spune litere ptr ghicire cuvant

while numar_vieti > 0:
    litera = input("Alege o litera: ").lower()
    # daca litera se afla in cuvant o inlocuim
    # daca utilizatorul introduce ami multe caractere afisam eroare
    if len(litera) > 1 or litera in "0123456789":
        print("Oops... Se pare ca ai introdus o cifra sau mai multe litere")
        continue
    elif litera in cuvant:
        print("se afla")
        cuvant_de_ghicit = list("".join(cuvant_de_ghicit).replace(" ", ""))
        for index, valoare in enumerate(cuvant):
            # daca litera introdusa este = cu litera din cuvant
            if litera == valoare:
                cuvant_de_ghicit[index] = litera
        cuvant_de_ghicit = " ".join(cuvant_de_ghicit)
        print(cuvant_de_ghicit)
        if "".join(cuvant_de_ghicit) == cuvant or "_" not in cuvant_de_ghicit:
            print(f"Ai castigat! Cuvantul era: {cuvant}")
            break
    else:
        numar_vieti = numar_vieti - 1
        if numar_vieti <= 0:
            print(f"Ai pierdut, cuvantul era: {cuvant}")