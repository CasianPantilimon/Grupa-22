import random

casute = "123456789"
casute_cu_spatii = " ".join(casute)
tabla_joc = casute_cu_spatii[0:5] + "\n" + casute_cu_spatii[6:11] + "\n" + casute_cu_spatii[12:]
print(tabla_joc)



for casuta in tabla_joc:
    casuta_user = input("- Este randul tau sa alegi o casuta: ")
    casute = casute.replace(casuta_user, "")
    print(casute)
    if casuta_user in tabla_joc:
        tabla_joc = tabla_joc.replace(casuta_user, "X")
        print(tabla_joc)
        # toate pozitiile castigatoare in functie de randuri
        if tabla_joc[0] == "X" and tabla_joc[2] == "X" and tabla_joc[4] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[6] == "X" and tabla_joc[8] == "X" and tabla_joc[10] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[12] == "X" and tabla_joc[14] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        # toate pozitiile castigatoare in functie de coloane
        elif tabla_joc[0] == "X" and tabla_joc[6] == "X" and tabla_joc[12] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[2] == "X" and tabla_joc[8] == "X" and tabla_joc[14] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[4] == "X" and tabla_joc[10] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        # diagonalele pentru X
        elif tabla_joc[0] == "X" and tabla_joc[8] == "X" and tabla_joc[16] == "X":
            print("HUMAN WINNNNS")
            break
        elif tabla_joc[4] == "X" and tabla_joc[8] == "X" and tabla_joc[12] == "X":
            print("HUMAN WINNNNS")
            break
        elif casute == "":
            print("Remiza. Nu mai sunt mutari disponibile.")

    casuta_PC = random.choice(casute)
    print(f"- Computerul a ales sa joace casuta: {casuta_PC}")
    casute = casute.replace(casuta_PC, "")
    if casuta_PC in tabla_joc:
        tabla_joc = tabla_joc.replace(casuta_PC, "0")
        print(tabla_joc)
        print(casute)
        if tabla_joc[0] == "0" and tabla_joc[2] == "0" and tabla_joc[4] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[6] == "0" and tabla_joc[8] == "0" and tabla_joc[10] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[12] == "0" and tabla_joc[14] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
            # toate pozitiile castigatoare in functie de coloane pentru 0
        elif tabla_joc[0] == "0" and tabla_joc[6] == "0" and tabla_joc[12] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[2] == "0" and tabla_joc[8] == "0" and tabla_joc[14] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[4] == "0" and tabla_joc[10] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
            # diagonalele pentru 0
        elif tabla_joc[0] == "0" and tabla_joc[8] == "0" and tabla_joc[16] == "0":
            print("PC WINNNNS")
            break
        elif tabla_joc[4] == "0" and tabla_joc[8] == "0" and tabla_joc[12] == "0":
            print("PC WINNNNS")
            break
        elif casute == "":
            print("Remiza. Nu mai sunt mutari disponibile.")


# pozitiile pe tabla de joc in functie de casute


# print(tabla_joc[0], "-0")
# print(tabla_joc[1], "-1")
# print(tabla_joc[2], "-2")
# print(tabla_joc[3], "-3")
# print(tabla_joc[4], "-4")
# print(tabla_joc[5], "-5")
# print(tabla_joc[6], "-6")
# print(tabla_joc[7], "-7")
# print(tabla_joc[8], "-8")
# print(tabla_joc[9], "-9")
# print(tabla_joc[10], "-10")
# print(tabla_joc[11], "-11")
# print(tabla_joc[12], "-12")
# print(tabla_joc[13], "-13")
# print(tabla_joc[14], "-14")
# print(tabla_joc[15], "-15")
# print(tabla_joc[16], "-16")