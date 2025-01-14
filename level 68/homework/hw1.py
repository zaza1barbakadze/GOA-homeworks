def increment_to_zeros(number):
    while True:
        # შეამოწმეთ, რომ ყველა ციფრი პირველის შემდეგ იყოს 0
        number_str = str(number)
        if all(digit == '0' for digit in number_str[1:]):
            return number
        # თუ არა, გაზარდეთ რიცხვი 1-ით
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

# პროგრამის გაშვება
main()