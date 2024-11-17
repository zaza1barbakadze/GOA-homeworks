def is_palindrome(number):
    return str(number) ==  str(number)[::-1]
def steps_to_palindrome(number):
    steps = 0
    while not is_palindrome(number):
        reversed_number = int(str(number)[::-1])
        number += reversed_number
        steps += 1
        return steps
    
    print(steps_to_palindrome(87))
    print(steps_to_palindrome(44))
    print(steps_to_palindrome(123))

    


