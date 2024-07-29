def function(nums):
    length = len(nums)
    for i in range(length - 1 ):
        if nums[i] == 0:
            for j in range( i + 1,length):
                if nums[j] != 0:
                    k = nums[i]
                    nums[i] = nums[j]
                    nums[j] = k
                    break
                else:
                    continue
    return nums


def func(nums):
    j = 0
    length = len(nums)
    for i in range(length):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for i in range(j,length):
        nums[i] = 0
    return nums


print(func([0,1,0,3,12]))