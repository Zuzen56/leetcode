def function(n):
    return n > 0 and (n & (n - 1 ))==0

print(function(32))