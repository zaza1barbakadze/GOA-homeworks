def filter_even_numbers(matrix):
    """
    იღებს 2D მასივს (matrix) და აბრუნებს ახალ 2D მასივს,
    რომელიც შეიცავს მხოლოდ ლუწ რიცხვებს.
    
    პარამეტრი:
    matrix (list of lists): ორ განზომილებიანი მასივი რიცხვებით

    აბრუნებს:
    list of lists: მასივი მხოლოდ ლუწი რიცხვებით
    """
    return [[num for num in row if num % 2 == 0] for row in matrix]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = filter_even_numbers(matrix)
print(result)
