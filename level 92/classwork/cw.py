import random

def random_element(arr):
    if not arr:
        return None
    return random.choice(arr)

my_list = [1, 2, 3, 4, 5]
print(random_element(my_list))