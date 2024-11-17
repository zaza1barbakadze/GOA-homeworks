def is_anagram(test, original):
    # აქ ვამოწმებთ თუ იმ შემთხვევაში, თუ ტესტის სიგრძე დიდია ორიგინალისასზე, მაშინ გვიბრუნებს 
    if len(test) != len(original): 
        return False

# აქ ვქმნით ახალ ცვლადს, რომელიც ორივეს უმატებს ერთმანეთს და პატარა ასოებით გვიწერს
    joined = (test + original).lower()

# ვიყენებთ for-ს რომ შევამოწმოთ ამ ახალ ცვლადში თითოეული სტრინგის სიგრძე ზუსტად იყოფა 2ზე თუ არა, თუ 2ზე ზუსდა იყოფა, ბრუნდება თრუე, თუ არა და ფალსი
    for char in joined:
        if joined.count(char) % 2 != 0:
            return False

    return True 