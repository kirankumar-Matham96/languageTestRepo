num = 12

def is_prime(number):
    if number == 0 or number == 1:
        return False
    
    for i in range(2, int(number/2)):
        if number%i == 0:
            return False
    return True

def print_fibonacci(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()

print(is_prime(num))
print(print_fibonacci(50))