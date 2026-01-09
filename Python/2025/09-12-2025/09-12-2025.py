def most_frequent(arr):
    liSet = list(set(arr))

    dic = {}
    for i in liSet:
        dic[i] = arr.count(i)

    print(max(dic, key=dic.get)) # https://note.nkmk.me/en/python-dict-value-max-min/


    return max(dic, key=dic.get)


most_frequent(["a", "b", "a", "c"])