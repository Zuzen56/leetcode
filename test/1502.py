def function(arr):
    length = len(arr)
    for i in range(length - 1 ):
        for j in range(length - 1 ,i, -1):
            if(arr[j] <arr[j - 1]):
                arr[j],arr[j - 1 ] = arr[j - 1 ],arr[j]
    d = arr[0] - arr[1]
    for i in range(length - 1):
        if arr[i]- arr[i + 1] != d:
            return False
    return True

print(function([1,2]))