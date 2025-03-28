def reverse_letter(s):
    return ''.join(c for c in s if c.isalpha())[::-1]

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("123abc!@#"))