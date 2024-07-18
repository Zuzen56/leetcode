def function(num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum = sum + num % 10
            num //= 10
        num = sum
    return num

print(function(708538619))