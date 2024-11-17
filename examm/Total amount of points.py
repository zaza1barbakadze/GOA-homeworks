def calculator_points(results):
    total_points = 0
    for result in results:
        x = int(result[0])
        y = int(result[2])
        if x > y :
            total_points += 3
        elif x == y:
            total_points += 1
            return total_points

თამაშები =  ["3:1", "2:2", "0:1", "4:0", "1:3", "2:2"]

points = calculator_points(თამაშები)

print(points)