def check_numbers(a, b):

    if a % 2 == 1 and a > b and b % 2 == 0:
        return True
    else:
        return False

print(check_numbers(7, 4))  
print(check_numbers(5, 6))  
print(check_numbers(8, 4))  
print(check_numbers(3, 1))  