def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


# a = make_list(101)
# print(a)
#
# b = list(range(50))
# print(b)

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield  a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)




