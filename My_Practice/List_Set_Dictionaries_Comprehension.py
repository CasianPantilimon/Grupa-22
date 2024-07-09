# a = ["a", "b", "c"]
# b = [1, 2, 3, 4]
#
# c = [a for a in b]
# print(c)
#
# my_list = [i for i in range(0, 100)]
#
# print(my_list)
#
# my_list3 = [i ** 2 for i in range(0, 100)]

##-----------------------------
# my_list4 = [i for i in range(0, 100) if i % 2 == 0]
# print((my_list4))
#
# # acelasi rezultat al liste 4 se poate produce si mai jos. se citeste mai usor dar
# # este in mai multe linii
#
# lista_numere = list(range(0, 100))
#
# def numere_pare():
#     lista_numere_pare = []  # Create an empty list to store even numbers
#     for i in lista_numere:
#         if i % 2 == 0:
#             lista_numere_pare.append(i)  # Append even numbers to the list
#     return lista_numere_pare  # Return the list of even numbers
#
#
# new_list = numere_pare()  # Call the function and store the result
# print(new_list)


##-----------------------------------------
## mai jos avem o lista de duplicate din care dorim sa extragem doar duplicatele
# si putem face asta in 3 moduri
#
# ## metoda 1
# some_list = ["a", "b", "b", "r", "b", "c", "c", "z", "x", "z"]
# duplicates = []
# for i in some_list:
#     if some_list.count(i) > 1:
#         if i not in duplicates:
#             duplicates.append(i)
#
# print(duplicates)
# ## metoda 2
# duplicates = list(set([i for i in some_list if some_list.count(i) > 1]))
# duplicates.sort()
#
# ## metoda 3
# print(duplicates)
# only_duplicates = set(duplicates)
# print(duplicates)
# print(only_duplicates)
# doar_duplicatele = list(only_duplicates)
# doar_duplicatele.sort()
# print(doar_duplicatele)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


a = list(range(100))
print(a)
print(make_list(51))

fruits = ("apple", "banana", "cherry")
print(fruits.index())
