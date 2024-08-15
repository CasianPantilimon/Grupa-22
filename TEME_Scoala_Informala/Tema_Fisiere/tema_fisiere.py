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

Cerințe suplimentare:

Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:

Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
Sortare: se alege o opțiune din cele 8 de mai jos:
Criteriile disponibile sunt:

1. sortare ascendentă task
2. sortare descendentă task
3. sortare ascendentă data
4. sortare descendentă data
5. sortare ascendentă persoana responsabilă
6. sortare descendentă persoană responsabilă
7. sortare ascendentă categorie
8. sortare descendentă categorie

Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la
tastatură. criteriile de filtrare sunt:
-       se cere de la tastatură câmpul după care se realizeaza filtrarea:

1. Task
2. Dată
3. Persoană responsabilă
4. Categorie

- după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea
 în lista inițială de date, astfel încât din lista inițială să rămână doar datele care conțin / încep
cu valoarea introdusă
- se afișează lista rămasă

4. Adăugarea unui nou task în lista inițială
5. Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de
      utilizator de la tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator
      unic pe rand, astfel încât să se știe ce informație urmează să editeze utilizatorul)

6. Ștergerea unui task din lista inițială.

Atenție! Trebuie să aveți grijă că o categorie poate să existe o singură dată (nu se accepta dubluri, ex curs,
cumpărături, muncă, cadouri, curs este greșit)

De asemenea, la adăugarea taskurilor se va avea grijă și la compararea textelor taskurilor, dacă textul
respectiv există, nu se poate adăuga.
"""