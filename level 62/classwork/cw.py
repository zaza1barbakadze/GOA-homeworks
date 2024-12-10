def bubble_sort(za):
    n = len(za)
    for i in range(n):
        for j in range(0, n-i-1):
            if za[j] > za[j+1]:
                za[j], za[j+1] = za[j+1], za[j]
    return za