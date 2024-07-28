# toate variabilele necesare

s = range(1, 10)
aa = range(0, 100)
ll = range(1, 13)
zz = range(1, 32)
jj = range(0, 47)
jj2 = range(51, 53)
nnn = range(0, 1000)
c = range(1, 10)

# stiu ca inca nu am folosit / invatat "range" dar din documentatia mea genereaza
# baza de date de care avem nevoie fara a o stoca in memorie

# si stiu ca lucreaza mai rapid decat listele. Practic ocupa mai putin spatiu in memorie
# ruland mai rapid. Acum nu este cazul dar cand bazele de date sunt mult mai largi, acolo unde une executii dau crash
# range() inca mai are spatiu sa lucreze

# ce vreau sa zic este ca list(range(0, 10000000)) va rula mult mai
# usor si rapid decat an actual list care are 10000000 de cifre

CNP = input("Introduceti un CNP valid: ")  # cerem CNP ul sub form de input, stocat ca si "str"

if len(CNP) != 13:
    print("CNP-ul trebuie să aibă exact 13 caractere.")  # cerem CNP ul sa aiba fix 13 caractere
else:
    # in loc de variabilele: s,aa,ll,zz,jj,jj2,nnn si c,
    # puteam folosi direct "range() urile in ""for loop uri" pentru a nu le mai stoca in memorie
    # dar imi place cum arata codul asa. HAȘTAG sorry not sorry =))
    if int(CNP[0]) not in s:
        print("Caracterul de pe indexul 1, nu este corect")
    elif int(CNP[1:3]) not in aa:
        print("Caracterele de pe indexul 2 și 3, nu sunt corecte")
    elif int(CNP[3:5]) not in ll:
        print("Caracterele de pe indexul 4 și 5, nu sunt corecte")
    elif int(CNP[5:7]) not in zz:
        print("Caracterele de pe indexul 6 și 7, nu sunt corecte")
    elif (int(CNP[7:9]) not in jj and int(CNP[7:9]) not in jj2) or CNP[7:9] == "00":
        # CNP[7:9] == "00" previne user ul de a itroduce 00 pe index ul CNP[7:9]
        print("Caracterele de pe indexul 8 și 9, nu sunt corecte")
    elif int(CNP[9:12]) in nnn and CNP[9:12] == "000":
        print("Caracterele de pe indexul 10, 11 și 12 nu sunt corecte")
    elif int(CNP[12]) not in c:
        print("Caracterul de pe indexul 13, nu este corect")
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

        print(f"{CNP} este un CNP valid. Persoana este de genul {gen}, "
              f"mai precis în anul '{an_nastere}, luna {luna_nastere}, "
              f"ziua {zi_nastere}.")

# S AA LL ZZ JJ NNN C
# X XX XX XX XX XXX X
# 0 12 34 56 78 9
#               10
#                 11
#                   12