def function(variables,target):
    ans = []
    for i, v in enumerate(variables):
        if pow(pow(v[0], v[1], 10), v[2], v[3]) == target:
            ans.append(i)
    return ans


print(function([[2,3,3,10],[3,3,3,1],[6,1,1,4]],2))