def get_bingo_letter(n):
    dic={
        "B":range(1,16),
        "I":range(16,31),
        "N":range(31,46),
        "G":range(46,61),
        "O":range(61,76)
    }
    #https://www.geeksforgeeks.org/python/python-get-key-from-value-in-dictionary/
    for key, val in dic.items():
        if n in val:
            print(key)
            return key

get_bingo_letter(75) # O
get_bingo_letter(54) # G
get_bingo_letter(25) #"I"
get_bingo_letter(38) # "N"
get_bingo_letter(11) #"B".