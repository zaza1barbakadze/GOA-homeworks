def progressive_concatenation(s):
    n = len(s)
    result = []
    
    for i in range(n // 2):
        result.append(s[i] + s[-(i + 1)] + str(i + 1))
    
    return "".join(result)

print(progressive_concatenation("abcdef"))
print(progressive_concatenation("abc!def"))
print(progressive_concatenation("abcd"))
print(progressive_concatenation("abcde"))