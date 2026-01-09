def compress_string(sentence):
    liSplit = sentence.split()
    liSet = list(set(liSplit))

    dic = {}
    for i in liSet:
        if (i in liSplit):
            count = liSplit.count(i)
            if (count > 1):
                dic[i] = count
                print(i, count)
            else:
                continue
    print(dic)

    sent = []
    for i in list(dict.fromkeys(liSplit)):
        if i in dic:
            sent.append(i + "(" + str(dic.get(i))+")")
        else:
            sent.append(i)

    result=" ".join(sent)
    print(result)
    return result


compress_string("I have have have apples")

compress_string("one one three and to the the the the")

compress_string("route route route route route route tee tee tee tee tee tee")