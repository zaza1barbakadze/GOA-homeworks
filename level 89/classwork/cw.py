import re

def count_letters_and_digits(s):
    return len(re.findall(r'[a-zA-Z0-9]', s))

print(count_letters_and_digits("hel2!lo"))  
print(count_letters_and_digits("wicked .. !"))  
print(count_letters_and_digits("!?..A"))  
