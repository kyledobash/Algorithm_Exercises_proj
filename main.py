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

