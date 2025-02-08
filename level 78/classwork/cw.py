def ელემენტი(matrix):
    lengths = []
    
    for row in matrix:
        for element in row:
            lengths.append(len(str(element)))

    return lengths

matrix = [
    [12, 345, 7],
    [89, 1, 4567]
]

result = ელემენტი(matrix)
print(result)  

