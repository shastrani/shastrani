def exponent(base, power):
    result = 1
    for index in range(power):
        result = result * base
    print(result)


exponent(3, 3)