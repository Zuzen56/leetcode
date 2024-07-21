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

def countGoodTriplets( arr, a, b, c):
    nums = 0
    for i in range(len(arr) - 2):
        j = i + 1
        for j in range(i + 1 ,len(arr) -1):
            k = j + 1
            for k in range(j + 1 ,len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            nums += 1
    return nums


print(numIdenticalPairs([1,1,1,1]))