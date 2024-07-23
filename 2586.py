def function(words,left,right):
    num = 0
    for i in range(left,right+1):
        str = words[i]
        if str[0] in "aeiou" and str[-1] in "aeiou":
            num += 1
    return num

print(function(["are","amy","u"],0,2))