def is_valid_hex(s):
    li_char = ["a", "b", "c", "d", "e", "f"]
    li_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    liBool = []

    if (len(s.split()) == 1 and s[0] == "#"):
        for i in list(s[1:].lower()):
            if (i in li_char) or (i in li_num):
                liBool.append(True)
            else:
                liBool.append(False)
        if (s[1:].isdecimal() and len(s[1:]) > 3):
            return False
        else:
            return all(liBool)
    else:
        return False


is_valid_hex("#12 3")  # True
is_valid_hex("#123abc")  # True
is_valid_hex("#ABCDEF")  # True.
is_valid_hex("#0a1B2c")  # True.
is_valid_hex("#12G")  # False.
is_valid_hex("#1234567")  # False
is_valid_hex("#12 3")  # False
is_valid_hex("fff")  # False