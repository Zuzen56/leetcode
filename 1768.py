def function(word1,word2):
    string = ""
    if len(word2) == len(word1):
        for i in range(len(word1)):
            string += word1[i]
            string += word2[i]

    if len(word2) < len(word1):
        for i in  range(len(word2)):
            string += word1[i]
            string += word2[i]
        for j in range(len(word2) , len(word1)):
            string += word1[j]

    if len(word2) > len(word1):
        for i in  range(len(word1)):
            string += word1[i]
            string += word2[i]
        for j in range(len(word1), len(word2)):
            string += word2[j]

    return string


def function2(word1,word2):
    string = ""
    l1 = len(word1)
    l2 = len(word2)
    index = 0
    while index < l1 or index < l2:
        if index < l1:
            string += word1[index]
        if index < l2 :
            string += word2[index]
            index += 1
    return string

print(function2("abcd" , "pqrer"))