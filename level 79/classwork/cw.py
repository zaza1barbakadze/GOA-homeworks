def is_flush(hand):
    suits = [card[-1] for card in hand]
    return len(set(suits)) == 1

print(is_flush(["AS", "3S", "9S", "KS", "4S"]))  
print(is_flush(["AD", "4S", "7H", "KS", "10S"]))