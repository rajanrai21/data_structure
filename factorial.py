def factorial_iterative(number):
    fact=1
    temp=1
    while temp <= number:
        fact*=temp
        temp+=1
    return fact

def factorial_recursive(number):
    if number == 0 or number ==1:
        return 1
    return number * factorial_recursive(number-1)

if __name__ == '__main__':
    print(factorial_iterative(8))
    print(factorial_recursive(2))
