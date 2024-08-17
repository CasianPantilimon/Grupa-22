"""
Se cere realizarea unui to-do list utilizând noțiunile învățate până în acest moment.
În prima faza se adaugă categoriile dorite de la tastatură:
exemplu: Introduceți categoriile de taskuri:
posibile răspunsuri: curs, cumpărături, muncă, cadouri, etc

 Cerințe:

-  se va cere, pe rand, introducerea unui task de la tastatura: ex: rezolvare tema
-  se va cere introducerea unei date limite de realizare a taskului respectiv, ex:  22.01.2022 21:30
-  se va adăuga o persoana responsabilă cu realizarea taskului respectiv: ex: Ion Vasile
-  se va adăuga o categorie din care taskul face parte. Ex. curs

Atenție, categoria trebuie să existe. În cazul în care nu există, se afișează mesaj de eroare.

Va exista posibilitatea de adăugare a unui număr nelimitat de taskuri, chiar si după ce utilizatorul confirmă faptul
că a terminat de introdus taskurile.

Datele se salveaza in fisiere. Vor exista doua fisiere: unul pentru categorii si unul care sa contina:
taskurile, data limita, persoana responsabila, categorie

"""
import time
import json


print("\n\rCooking stuff for you...", end="")
time.sleep(3)
print("\rinca un pic...👉👈 ", end="")
time.sleep(2)
print("\rGata 🎉🎉🎉", end="")
time.sleep(1)
print("\r ",)

for i in range(7):
    if i % 2 == 0:
        print("\r⚡ Welcome to my To-Do List ⚡",end="",)
        time.sleep(0.3)
    else:
        print("\r ",end="")
        time.sleep(0.3)


categorii = []
tasks = {}

while True:
    meniu_imput = input("\nMeniu Optiuni:\n"
                        "1. Adauga o categorie "
                        "\n2. Editare categorie "
                        "\n    - adaugare task "
                        "\n    - data limita"
                        "\n    - persoana responsabila"
                        "\n3. Afisare categorii"
                        "\n4. Afisare taskuri, data limita si persoana responsabila "
                        "pentru o categorie"
                        # "\n -> optiuni extra "
                        "\n5. Exit"
                        "\n"
                        "\nOptiunea aleasa: ")

    if meniu_imput == "1":
        while True:
            print("- Pentru a te intoarce la meniul initial, press '1'.")
            print("- Pentru a afisa categoriile existente, press '2'.")
            categorie = input("Introduceti o categorie: ")
            if categorie == "1":
                break
            if categorie == "2":
                print("Afisare categorii... ")
                time.sleep(1)
                print(categorii, "\n")
                continue

            print("\nAdaugare categorie...")
            categorii.append(categorie)
            with open("categorii.txt", "w+") as my_file:
                json.dump(categorii, my_file)
            time.sleep(1)
            print("Categorie adaugata cu succes!\n")
            continue

    elif meniu_imput == "2":
        while True:
            print("- Pentru a te intoarce la meniul initial, press '1'.")
            print("- Pentru a afisa taskurile existente, press '2'.")
            print("- Pentru a afisa categoriile existente, press '3'.")
            task = input("Adauga un task.\nDenumire task: ")
            if task == "1":
                print("\nIntoarcere la meniul principal...\n")
                time.sleep(1)
                break
            if task == "2":
                print("\nAfisare taskuri existente...\n")
                time.sleep(1)
                print(tasks)
                continue
            if task == "3":
                print("\nAfisare categorii existente...\n")
                time.sleep(1)
                print(categorii)
                continue

            data_limita = input("Introdu data limita: ")
            if data_limita == "1":
                print("\nIntoarcere la meniul principal...\n")
                time.sleep(1)
                break
            if data_limita == "2":
                print("\nAfisare taskuri existente...\n")
                time.sleep(1)
                print(tasks)
                continue

            persoana_asignata = input("Introdu persoana asignata: ")
            if persoana_asignata == "1":
                print("\nIntoarcere la meniul principal...\n")
                time.sleep(1)
                break
            if persoana_asignata == "2":
                print("\nAfisare taskuri existente...\n")
                time.sleep(1)
                print(tasks)
                continue

            if task not in tasks.keys():
                alegere_categorie = input(f"Categorii disponibile: {categorii}."
                                          f"\nAlege o categorie in care doresti sa adaugi task-ul: ")
                if alegere_categorie in categorii:
                    print("Procesare Task...")
                    tasks[alegere_categorie] = [task, data_limita, persoana_asignata]
                    time.sleep(1)
                    print("Task creat cu succes!")
                    with open("tasks.txt", "w+") as my_file:
                        json.dump(tasks,my_file)

                else:
                    print("Categoria nu exista")

    # elif int(meniu_imput) == 3:
    #     data_limita = input("Introduceti o data limita: ")
    # elif int(meniu_imput) == 4:
    #     peroana_responsabila = input("Introduceti o persoana responsabila: ")
    elif meniu_imput == "3":
        print(categorii)
        while True:
            optiune = input("\n- Pentru a te intoarce la meniul initial, press '1'. ")
            if optiune == "1":
                print("\nIntoarcere la meniul principal...\n")
                time.sleep(1)
                break
            else:
                print("Optiunea nu exista!")
    elif meniu_imput == "4":
        print(tasks)
        while True:
            optiune = input("\n- Pentru a te intoarce la meniul initial, press '1'. ")
            if optiune == "1":
                print("\nIntoarcere la meniul principal...\n")
                time.sleep(1)
                break
            else:
                print("Optiunea nu exista!")
    elif meniu_imput == "5":
        print("Closing the list...")

        break
    else:
        print("Optiunea nu exista!")
        continue
