# MAP, FILTER< ZIP and Reduce

# MAP
my_list = [1, 2, 3, ]

new_list = [7, 8, 9, ]

lista_nume = ["Anna", "Bonny", "aurelia", "Anastasia", "Amalia", "anusca"]


def multiply_by2(item):
    return item * 2


def uneven_numbers(item):
    return item[0] == "A"


def strings_selection(item):
    strings_selection_list = []

    if item[0] == "A" or "a":
        return item
    return strings_selection_list.append(item)


def a_names(item):
    return item[0] == "A"


# print(list(filter(a_names, lista_nume)))


# print(strings_a)
# print(my_list)
# print(list(map(multiply_by2, my_list)))
# print(list(map(multiply_by2, my_list)))
# print(list(map(multiply_by2, my_list)))

# print(list(filter(uneven_numbers, name_list)))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_str(i):
    return i.capitalize()


print(list(map(capitalize_str, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(tuple(zip(my_strings, my_numbers)))
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def above_50(item):
    return item > 50


print(list(filter(above_50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

total_scores = sum(scores)
total_my_numbers = sum(my_numbers)

total = total_scores + total_my_numbers



