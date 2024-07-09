operatii_matematice = "+-*/"
operator_1 = input("Care este primul operator?: ")

stare_conversie = True
for element in operator_1:
    if element in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        print(element, "operator_1")
        stare_conversie = False
        break
if stare_conversie is True:
    operator_2 = input("Care este al doilea operator?: ")

    for element in operator_2:
        if element in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            print(element, "operator_2")
    # daca putem converti, realizam conversie

    if stare_conversie is True:
        operatie = input("Introdu operatia dorita (+-*/): ")
        operator_1_convertit = float(operator_1)
        operator_2_convertit = float(operator_2)
        # print("putem efectua operatiile")
        # aici putem efectua
        # daca operatia introdusa
        if len(operatie) == 1 and operatie in "+-*/":
            rezultat = None
            # daca operatorul este + facem adunare
            if operatie == "+":
                rezultat = operator_1_convertit + operator_2_convertit
                print(rezultat)
            # daca operatorul este - facem scadere
            elif operatie == "-":
                rezultat = operator_1_convertit - operator_2_convertit
                print(rezultat)
            # daca operatorul este * facem inmultire
            elif operatie == "*":
                rezultat = operator_1_convertit * operator_2_convertit
                print(rezultat)
            # daca operatorul este / facem imaprtire
            elif operator_2 != 0.0:
                rezultat = operator_1_convertit / operator_2_convertit
                print(rezultat)
            print(
                f"Operatorul 1 este: {operator_1_convertit}, iar operatorul 2 este: {operator_1_convertit}.Rezultatul este {rezultat}")

# All changes deleted
