def signFunc(x):
    if x == 0:
        return 0
    elif x > 0 :
        return 1
    else:
        return -1

def function(nums):
    product = 1
    for i in nums :
        product *= i
    return signFunc(product)


print(function([-1,-2,-3,-4,3,2,1]))