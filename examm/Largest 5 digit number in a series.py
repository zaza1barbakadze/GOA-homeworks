def five_digit_sequence(number):
    max_sequence = "0"
    for i in range(len(number) - 4):
        current_sequence = number [i:i +5]
        if current_sequence > max_sequence:
            max_sequence > current_sequence
            return int(max_sequence)
        
print(five_digit_sequence("283910"))
print(five_digit_sequence("1234567890"))
print(five_digit_sequence("156135344"))