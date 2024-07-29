def function(n):
    sum = 0
    num = 1
    middle = n
    while n > 0:
        sum += n % 10
        n //= 10

    n = middle

    while n > 0:
        num *= n % 10
        n //= 10

    return num - sum

# def function(n):
#     a = 0
#     b = 1
#     while n > 0:
#         x , n = n % 10,n // 10
#         a += x
#         b *= x
#     return b - a


print(function(114))