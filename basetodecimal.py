def anyBaseToDecimal(number, base):
    iterator = 0
    decimal = 0

    while number > 0:
        lastDigit = number % 10
        decimal += lastDigit * base ** iterator
        iterator += 1
        number //= 10

    return decimal


if _name_ == "_main_":
    A = int(input())
    B = int(input())

    print(anyBaseToDecimal(A, B))