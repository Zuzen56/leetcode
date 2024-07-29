def function(n):
    while n > 1 and n != 1:
        if n % 3 != 0:
            return bool(0)
        n //= 3
    return bool(1) and n > 0

def isPowerOfThree(num):
    while num and num % 3 == 0:
        num //= 3
    return num == 1



print(function(24))
print(isPowerOfThree(24))