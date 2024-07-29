def function(s):
    max = 0
    if len(s) <= 2:
        if s =="0" or s =="1" or s == "11" or s == "00":
            return 1
        if s == "01":
            return  2
        if s == "10":
            return 0

    for i in range(1,len(s)):
        s1 = s[:i]
        s2 = s[i:]
        sum = 0
        for j  in s1:
            if j == '0':
                sum += 1
        for k in s2:
            if k == '1':
                sum +=1
        if sum >= max  :
            max = sum
    return max

def function2(s):
    return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))

print(function("01001"))