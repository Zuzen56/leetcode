def function(points,w):
    points.sort()
    nums = 0
    bound = -1
    for point in points:
        if point[0] > bound:
            bound = point[0] + w
            nums += 1
    return nums

print(function([[1,3],[8,8]],2))