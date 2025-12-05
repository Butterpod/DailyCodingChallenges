def difference(arr1, arr2):
    liContains = []

    for i in arr1:
        if i not in arr2:
            print("Je suis LA : ", i)
            liContains.append(i)

    for i in arr2:
        if i not in arr1:
            print("Je suis LA : ", i)
            liContains.append(i)

    print(liContains)

    return liContains
