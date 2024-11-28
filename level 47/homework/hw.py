def convert_minutes_to_seconds(minutes):
    """
    გადაიყვანე წუთები წამებად.
    
    Args:
        minutes (int ან float): წუთების რაოდენობა.
    
    Returns:
        int: შესაბამისი წამების რაოდენობა.
    """
    return int(minutes * 60)

# მაგალითი გამოყენებისთვის:
minutes = 5
seconds = convert_minutes_to_seconds(minutes)
print(f"{minutes} წუთი არის {seconds} წამი.")