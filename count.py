import math

def count_iterateve(number):
    result=0
    while number != 0:
        number//=10
        result+=1
    return result

def count_recursive(number):
    if number == 0:
        return 0
    return 1 + count_recursive(number//10)

def count_constant(number):
    return math.floor(math.log10(number)+1)

if __name__ == "__main__":
    print(count_iterateve(123))
    print(count_recursive(54321))
    print(count_constant(123945645))
