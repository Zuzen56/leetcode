def function(nums,n):
    nums2 = nums[0:n]
    nums1 = nums[n:2*n]
    for i in range(2*n):
        if i % 2 != 0:
            j = int((i - 1)/2)
            nums[i] = nums1[j]
        else:
            j =  int(i // 2)
            nums[i] = nums2[ j ]

    return nums

print(function([1,2,3,4,5,6] ,3))