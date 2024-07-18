def function(n):
    while n > 1 and n != 1:
        while n > 1 and n != 1:
            while n > 1 and n != 1:
                if n % 2 != 0:
                    return bool(0)
                n //= 2
            if n % 3 != 0:
                return bool(0)
            n //= 3
        if n % 5 != 0:
            return bool(0)
        n //= 5
    return bool(1) and n > 0

print(function(100))