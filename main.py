import numpy as np


def create_phone_number(n):
    number_array = []
    number_array.append("(")
    number_array.append(n[0])
    number_array.append(n[1])
    number_array.append(n[2])
    number_array.append(")")
    number_array.append(" ")
    number_array.append(n[3])
    number_array.append(n[4])
    number_array.append(n[5])
    number_array.append("-")
    number_array.append(n[6])
    number_array.append(n[7])
    number_array.append(n[8])
    number_array.append(n[9])

    phone_number_array = map(str, number_array)
    phone_number = "".join(phone_number_array)

    return phone_number


def create_phone_number_refactored(n):
    n.insert(0, "(")
    n.insert(4, ") ")
    n.insert(8, "-")

    phone_number_array = map(str, n)
    phone_number = "".join(phone_number_array)

    return phone_number


print(create_phone_number_refactored([6, 0, 2, 9, 9, 9, 4, 2, 9, 8]))


def count_bits(n):
    counter = 0
    input_binary = bin(n)
    for digit in input_binary:
        if digit == "1":
            counter += 1

    return counter


print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))


# def to_camel_case(text):
#     result = ""
#
#     for i in range(0, len(text)):
#         if i > len(text):
#             return result
#         elif text[i] != "-" and text[i] != "_":
#             result = result + text[i]
#         else:
#             result = result + text[i + 1].upper()
#             text = text.replace(text[i + 1], "")
#
#     return result
#
#
# print(to_camel_case("kyle-dobash"))


def filter_list(l):
    result = []
    for element in l:
        if isinstance(element, str):
            continue;
        else:
            result.append(element)

    return result


print(filter_list([1,2,'a','b']))


def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)

    if len(result) == 0:
        return str(integer) + " is prime"
    else:
        return result


print(divisors(13))


# def is_valid_walk(walk):
#     counter = 0
#
#     for direction in walk:
#         counter += 1
#
#     if counter * 2 == 10:
#         return True
#     else:
#         return False
#
# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
# print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
# print((['w']), 'should return False')
# print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False')

