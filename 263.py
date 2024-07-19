def function(n):
    if n <= 0:
        return False
    s = [2,3,5]
    for i in s :
        while n % i == 0:
            n //= i
    return n == 1

print(function(6))