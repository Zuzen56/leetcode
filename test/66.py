def function(digits):
    i = len(digits) - 1
    while i > -1:
        if digits[i] < 9 :
            digits[i] += 1
            break
        else:
            digits[i] = 0
            if i == 0:
                return [1] + digits
        i -= 1
    return digits

def func(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            for j in range(i + 1, n):
                digits[j] = 0
            return digits

    # digits 中所有的元素均为 9
    return [1] + [0] * n




print(func([4,3,2,9]))