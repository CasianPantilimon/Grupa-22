# my_list = [5, 4, 3, ]
# # In loc sa folosim o functie pentru a multiplica numerele
# # def multiply_by_two(item):
# #     return item * 2
# # putem folosi LAMBDA pentru a crea o functie "one time use". Odata ce este rulata Python o sterge din memorie
# print(list(map(lambda item: item * 2, my_list)))
#
# print(list(map(lambda item: item ** 2, my_list)))
# #  mai jos lista a va fi sortata prima data dupa al doilea item al fiecariu tuplu iar apoi dupa primul item al
# #  fiecariu tuplu
# a = [(0, 2), (4, 3), (9, 9), (2, 6), (10, -1)]
# print(a)
# a.sort(key=lambda y: y[1])
# print(a)
# a.sort()
# print(a)
# # print(list(map(lambda item: item ** 2, a)))
#
#
