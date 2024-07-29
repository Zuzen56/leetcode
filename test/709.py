def function(s):
    string = ""
    for i in s:
        i = ord(i)
        i = int(i)
        if i<= 90 and i >=65:
            i = i + 32
            i = chr(i)
            string = string + i
        else:
            i = chr(i)
            string = string + i
    return string

#def function(s):
#    return s.lower()

print(function("loWERcAse"))