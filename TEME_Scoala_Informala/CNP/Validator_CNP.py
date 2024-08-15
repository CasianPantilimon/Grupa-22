# CNP = input("Introduceti un CNP valid: ")  # cerem CNP ul sub form de input, stocat ca si "str"


def validator_CNP(CNP):
    if len(CNP) != 13:
        print("CNP-ul trebuie să aibă exact 13 caractere.")  # cerem CNP ul sa aiba fix 13 caractere
        quit()  # otherwise we will quite at once

    if len(CNP) == 13:
        control = "279146358279"
        cifra_control = []
        list_control = [int(i) for i in control]  # facem o lista cu caracterele din "control"
        list_CNP = [int(i) for i in CNP]  # facem o lista cu caracterele din "CNP"
        mixed = list(zip(list_control, list_CNP))  # le unim ca si tupluri
        for i in mixed:
            multiplied = i[1] * i[0]  # le inmultim
            cifra_control.append(multiplied)

        inmultite = [2, 63, 72, 0, 20, 12, 18, 10, 56, 2, 42, 81]
        cifra_control = (sum(inmultite) % 11)  # and this will be the ALL MIGHTY C

        if int(CNP[0]) not in range(1, 10):
            return "Caracterul de pe indexul 1, nu este corect."
        elif int(CNP[1:3]) not in range(0, 100):
            return "Caracterele de pe indexul 2 și 3, nu sunt corecte."
        elif int(CNP[3:5]) not in range(1, 13):
            return "Caracterele de pe indexul 4 și 5, nu sunt corecte."
        elif int(CNP[5:7]) not in range(1, 32):
            return "Caracterele de pe indexul 6 și 7, nu sunt corecte."
        elif (int(CNP[7:9]) not in range(0, 47) and int(CNP[7:9]) not in range(51, 53)) or CNP[7:9] == "00":
            # CNP[7:9] == "00" previne user ul de a itroduce 00 pe index ul CNP[7:9]
            return "Caracterele de pe indexul 8 și 9, nu sunt corecte."
        elif int(CNP[9:12]) in range(0, 1000) and CNP[9:12] == "000":
            return "Caracterele de pe indexul 10, 11 și 12 nu sunt corecte."
        elif int(CNP[12]) != cifra_control:
            if int(CNP[12]) != cifra_control:
                return "Caracterul de pe indexul 13, nu este corect."
            else:
                return "Caracterul de pe indexul 13, este corect."
        else:
            # acum ca avem un CNP valid, putem sa verificam si ce inseamna numere,
            # aflad genul, anul, luna si ziua in care s a nascut persoana
            if CNP[0] == "1":
                gen = "masculin, născut între 1 ianuarie 1900 și 31 decembrie 1999"
            elif CNP[0] == "2":
                gen = "feminin, născută între 1 ianuarie 1900 și 31 decembrie 1999"
            elif CNP[0] == "3":
                gen = "masculin, născut între 1 ianuarie 1800 și 31 decembrie 1899"
            elif CNP[0] == "4":
                gen = "feminin, născută între 1 ianuarie 1800 și 31 decembrie 1899"
            elif CNP[0] == "5":
                gen = "masculin, născut între 1 ianuarie 2000 și 31 decembrie 2099"
            elif CNP[0] == "6":
                gen = "feminin, născută între 1 ianuarie 2000 și 31 decembrie 2099"
            elif CNP[0] == "7":
                gen = "masculin, fiind o persoană străină rezidentă în România"
            elif CNP[0] == "8":
                gen = "feminin, fiind o persoană străină rezidentă în România"
            elif CNP[0] == "9":
                gen = "persoană străină"

            an_nastere = CNP[1:3]

            if CNP[3:5] == "01":
                luna_nastere = "Ianuarie"
            elif CNP[3:5] == "02":
                luna_nastere = "Februarie"
            elif CNP[3:5] == "03":
                luna_nastere = "Martie"
            elif CNP[3:5] == "04":
                luna_nastere = "Aprilie"
            elif CNP[3:5] == "05":
                luna_nastere = "Mai"
            elif CNP[3:5] == "06":
                luna_nastere = "Iunie"
            elif CNP[3:5] == "07":
                luna_nastere = "Iulie"
            elif CNP[3:5] == "08":
                luna_nastere = "August"
            elif CNP[3:5] == "09":
                luna_nastere = "Septembrie"
            elif CNP[3:5] == "10":
                luna_nastere = "Octombrie"
            elif CNP[3:5] == "11":
                luna_nastere = "Noiembrie"
            elif CNP[3:5] == "12":
                luna_nastere = "Decembrie"

            zi_nastere = CNP[5:7]

            return (f"{CNP} este un CNP valid. "
                    f"Persoana este de genul {gen} mai precis în anul '{an_nastere}, "
                    f"luna {luna_nastere}, ziua {zi_nastere}.")


print(validator_CNP("1980526271694"))
