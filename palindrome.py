def palindrome(num):
    rev = 0
    temp = num
    while temp != 0:
        rem = temp%10
        temp = temp//10
        rev = rev*10+rem
    return num == rev

if __name__  == '__main__':
    print(palindrome(int(input())))
