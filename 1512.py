def numIdenticalPairs( nums):
    j = 1
    result = 0
    for i in range(len(nums) - 1):
        while j < len(nums) :
            if (nums[i] == nums[j]) & (i < j):
                result += 1
            j += 1
        i += 1
        j = i + 1
    return result

print(numIdenticalPairs([1,1,1,1]))