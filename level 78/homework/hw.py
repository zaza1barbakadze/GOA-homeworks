def two_sum(numbers, target):
    num_indices = {}
    
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in num_indices:
            return (num_indices[complement], index)
        num_indices[num] = index
    
    return None 

print(two_sum([1, 2, 3], 4))  
print(two_sum([3, 2, 4], 6))  