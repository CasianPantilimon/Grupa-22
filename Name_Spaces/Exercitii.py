# # print(dir(__builtins__))
# var = 1
# def functie2() -> str:
#     global var
#     var = 3
#     print(var, 'functie2')
#     return var
# def functie() -> str:
#     msg = "Hello"
#     print(msg)
#     global var
#     print(var, 'in functie inainte de reasignare valoare')
#     var = 2
#     print(var, 'in functia functie')
#     return msg
#
# print(var)
# functie2()
# functie()
# print(var, 'global in fisier')
#
#
# def functie1():
#     def functie2():
#         global msg
#         msg = 'Hello2'
#         print(f"functie secundara: {msg}")
#     msg = 'Hello'
#     print(f"functie: {msg}")
#     functie2()
#
#
# msg = 'hello3'
# print(msg)
# functie1()
# print(msg)