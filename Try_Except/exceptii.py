# my_var = input("Adauga un numar: ")
#
# try:
#     conversie_int = int(my_var)
# except ValueError as err:
#     print(err)
#
#
#
# my_var = input("Adauga un numar: ")
# try:
#     conversie_int = int(my_var)
#     a = int(input("a doua valoare: "))
#     impartire = conversie_int / a
#     print(variabila)
# except ValueError:
#     print("eroare de valoare")
# except NameError:
#     print('variabila nu este declarata')
#     variabila = None
# except ZeroDivisionError:
#     print("Impartirea la zero nu este permisa")
#     while a == 0:
#         a = int(input("A doua valoare: "))
#     impartire = conversie_int / a
#     print(impartire)
# except Exception as e:
#     print(e)
# else:
#     print("Codul nu are exceptii")
# finally:
#     print("se executa indiferent")
# print(variabila)
#
#
# """
# Sa se acceseze un element dintr-o lista dupa indexul specificat de utilizator.
# Folosim try-except pentru a gestiona lipsa unui index din lista.
# """
# lista = [1, 2, 3, 4, 5]
# try:
#     valoare_index = int(input("Introduceti indexul: "))
#     print(lista[valoare_index])
# except IndexError:
#     print("Indexul este in afara limitelor listei")
#     while valoare_index > len(lista) - 1:
#         valoare_index = int(input("Introduceti indexul: "))
#     print(lista[valoare_index])

"""
sa se acceseze o valoare intr-un dictionar dupa cheia specificata de utilizator.
Folosim try-except pentru a gestiona cazul in care cheia nu exista in dictionar
"""
# dictionar = {'Angajat1': 1, 'Angajat2': 2, 'Angajat3': 3}
#
# try:
#     cheie = input("Introduceti angajatul pentru care doriti sa vizualizati numar de zile de concediu: ").capitalize()
#     print(dictionar[cheie])
# except KeyError:
#     print('Angajatul nu exista. Acesta este un angajat nou. Adaugati nr de zile de concediu')
#     dictionar[cheie] = 21
#     print(dictionar[cheie])
#     print(dictionar)
# # print(dictionar.get(cheie))

# """
# se cere introducerea unui numar pe care dorim sa il convertim in float.
# Folosim try-except pentru a trata cazul in care introducem de la tastatura un string.
# """
#
#
# def verificare_cifre(numar_de_verificat: str) -> bool:
#     for i in numar_de_verificat:
#         if i not in '0123456789.':
#             return False
#     return True
#
#
# try:
#     numar = input("Introdu un numar: ")
#     numar = float(numar)
#     print(numar)
# except ValueError:
#     print("Nu ati introdus un numar")
#     while verificare_cifre(numar) is False:
#         numar = input("Introdu un numar: ")
#     numar = float(numar)
#     print(numar)

