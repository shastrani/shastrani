def factorials(num1):
    result = 1
    for index in range(1, num1 + 1):
        result = result * index
    return result

print(factorials(5))
