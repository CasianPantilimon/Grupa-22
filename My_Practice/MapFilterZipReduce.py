# MAP, Filter, ZIP and reduce
my_list = [1, 2, 3]


def multiply_by_two(item):
    return item * 2


print(list(map(multiply_by_two, my_list)))
print(my_list)  # se poate observa ca lista initiala nu a fost modificata
my_list = ["anna", "mere", "pere"]


def capitalize_word(item):
    return item.capitalize()


print(list(map(multiply_by_two, my_list)))

# FILTER
my_list = [1, 2, 3]


def numere_impare(item):
    return item % 2 != 0


print(list(filter(numere_impare, my_list)))

lista_nume = ["Anna", "Bonny", "aurelia", "Anastasia"]


def a_names(item):
    return item[0] == "A"


print(list(filter(a_names, lista_nume)))

# ZIP
phone_number_list = [4075412146, 4072147592, 40754353584, 4075289636]
email_list = ["gandalf@gmail.com", "Bonnie@gmail.com", "tudor@gmail.com", "sally@gmail.com"]
age_tuple = (44, 20, 30, 12)

print(list(zip(phone_number_list, email_list, age_tuple)))
# din nou ZIP nu va modifica nici una dintre liste, which is ***AWESOMEEE***
