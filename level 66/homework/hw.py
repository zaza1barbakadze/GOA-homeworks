def element(zaza):
    from collections import Counter
    element_counts = Counter(zaza)
    return [item for item, count in element_counts.items() if count == 1]

input_array = [1, 2, 2, 3, 4, 4, 5]
unique_elements = element(input_array)
print(unique_elements) 