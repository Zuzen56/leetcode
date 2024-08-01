def function(moves):
    result = [0,0]
    for i in moves:
        if i == "L":
            result[0] -= 1
        if i == "R":
            result[0] += 1
        if i == "U":
            result[1] += 1
        if i == "D":
            result[1] -= 1

    return result == [0,0]

print(function("UD"))