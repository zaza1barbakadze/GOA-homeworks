while True:
    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

        result = num1 * num2
        print(f"ნამრავლი არის: {result}")

        command = input("თუ გსურთ პროგრამიდან გამოსვლა, შეიყვანეთ 'exit', თუ არა - სხვა რამ: ")
        if command.lower() == 'exit':
            print("პროგრამა დასრულდა.")
            break
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვები.")
