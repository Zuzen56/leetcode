def function(arr):
    index = 0
    length = len(arr)
    max = -1
    for i in range(length):
        if arr[i] > max:
            max = arr[i]
            index += 1
            if max > arr[i + 1]:
                return index - 1


print(function([0,1,7,6,0]))