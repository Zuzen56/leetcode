def function(accounts):
    max = 0
    for i in accounts:
        if sum(i) > max:
            max = sum(i)
    return max
print(function([[1,5],[7,3],[3,5]]))