def generate_2d_array(rows, cols):

    array = []
    current_number = 1

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(current_number)
            current_number += 1
        array.append(row)

    return array

result = generate_2d_array(2, 2)
print(result)
