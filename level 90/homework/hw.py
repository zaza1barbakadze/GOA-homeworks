def categorize_members(members):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in members]

input_data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output_data = categorize_members(input_data)
print(output_data)