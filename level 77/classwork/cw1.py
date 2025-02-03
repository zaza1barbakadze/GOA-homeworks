def calculate_points(matches):
    points = 0
    for match in matches:
        x, y = map(int, match.split(":"))
        if x > y:
            points += 3  #მოგება
        elif x < y:
            points += 0  #წაგება
        else:
            points += 1  #ფრე
    return points