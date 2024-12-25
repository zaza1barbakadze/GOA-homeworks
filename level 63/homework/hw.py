def jeyrani(player1, player2):
    valid_moves = ["ქვა", "მაკრატელი", "ფურცელი"]
    if player1 not in valid_moves or player2 not in valid_moves:
        return "Invalid move! Players must choose 'ქვა', 'მაკრატელი', or 'ფურცელი'."
    
    if player1 == player2:
        return "ფრეა!"
    
    if (player1 == "ქვა" and player2 == "მაკრატელი") or \
       (player1 == "მაკრატელი" and player2 == "ფურცელი") or \
       (player1 == "ფურცელი" and player2 == "ქვა"):
        return "Player 1 იმარჯვებს!"
    else:
        return "Player 2 იმარჯვებს!"

print(jeyrani("ქვა", "მაკრატელი"))  
print(jeyrani("მაკრატელი", "ფურცელი")) 
print(jeyrani("ფურცელი", "ფურცელი"))   
