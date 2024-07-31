def function(nums):
    result = []
    length = len(nums)
    if length == 1:
        return True
    for i in range(length - 1):
        result.append(nums[i] - nums[i + 1])
    array_all_positive = [x >= 0 for x in result]
    array_all_negative = [x <= 0 for x in result]

    if all(array_all_positive) or all(array_all_negative):
        return True
    else:
        return False

def function2(nums):
    length = len(nums)
    inres = True
    deres = True
    for i in range(length - 1 ):
        if nums[i] > nums[ i + 1]:
            inres = False
        if nums[i] < nums[i + 1]:
            deres = False
    return  inres or deres

print(function2([1,3,2]))