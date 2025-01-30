from bisect import bisect_left

def count_smaller_numbers_to_right(arr):
    result = []
    sorted_list = []
    
    for num in reversed(arr):
        index = bisect_left(sorted_list, num)
        result.append(index)
        sorted_list.insert(index, num)
    
    return result[::-1]

print(count_smaller_numbers_to_right([5, 4, 3, 2, 1]))
print(count_smaller_numbers_to_right([1, 2, 0]))
