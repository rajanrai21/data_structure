def factorial_last_zero(number):
    fact=1
    temp=1
    while temp <= number:
        fact*=temp
        temp+=1
    print(fact)
    count = 0
    while fact%10 == 0:
        fact //= 10
        count += 1
    return count

def fau(number):
    count=0
    i = 5;
    while i <= number:
        count+=number//i
        i*=5
    return count


if __name__ == '__main__':
    print(fau(0))
