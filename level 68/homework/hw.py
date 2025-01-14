def text_input_suggestion():
    entered_texts = set()

    while True:
        text = input("შეიყვანეთ ტექსტი (ან დააჭირეთ Enter-ს გამოსასვლელად): ").strip()
        
        if not text:
            print("პროგრამა დასრულდა. ნახვამდის!")
            break
        
        if text in entered_texts:
            print(f"თქვენ უკვე შეყვანილი გაქვთ '{text}'. სცადეთ სხვა ტექსტი!")
        else:
            print(f"თქვენ შეყვანეთ '{text}'.")
            entered_texts.add(text)

text_input_suggestion()