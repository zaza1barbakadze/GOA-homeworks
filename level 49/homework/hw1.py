def create_multiplication_table():
    table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
    return table

multiplication_table = create_multiplication_table()
for row in multiplication_table:
    print(row)