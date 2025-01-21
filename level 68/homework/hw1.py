def increment_to_zeros(number):
    while True:
        number_str = str(number)
        if all(digit == '0' for digit in number_str[1:]):
            return number
        number += 1

def main():
    try:
        user_input = int(input("შეიყვანეთ რიცხვი: "))
        if user_input < 0:
            print("გთხოვთ შეიყვანოთ დადებითი რიცხვი.")
            return

        result = increment_to_zeros(user_input)
        print(f"შედეგი: {result}")
    except ValueError:
        print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")

main()