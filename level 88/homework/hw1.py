def compare_even_odd(s: str) -> str:
    even_sum = sum(int(d) for d in s if int(d) % 2 == 0)
    odd_sum = sum(int(d) for d in s if int(d) % 2 != 0)

    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"

print(compare_even_odd("123456"))
print(compare_even_odd("13579"))
print(compare_even_odd("112233"))