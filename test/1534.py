def function(array,a,b,c):
    length = len(array)
    nums = 0
    for i in range(length - 2):
        j = i + 1
        while j < length -1:
            k = j + 1
            while k < length:
                if abs(array[i] - array[j]) <= a:
                    if abs(array[j] - array[k]) <= b:
                        if abs(array[i] - array[k]) <= c:
                            nums += 1
                k += 1
            j += 1
    return nums

print(function([3,0,1,1,9,7],7,2,3))