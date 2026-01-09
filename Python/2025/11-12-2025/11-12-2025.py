def to_roman(num):
    dic = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000}

    print(dic.values())
    liRoman = []

    print(num // 1000)
    if (num // 1000 < 5):
        res = num // 1000
        # print(dic.get("X")*res)
        mille = list(dic.keys())[list(dic.values()).index(1000)] * res
        liRoman.append(mille)
        num -= 1000 * res
        print("JE SUIS LA :", num)

    print("d", num)
    if (num // 500 == 1):
        # print(dic.get("X")*res)
        cinqCent = list(dic.keys())[list(dic.values()).index(500)]
        liRoman.append(cinqCent)
        num -= 500

    if (num // 400 == 1):
        # print(dic.get("X")*res)
        cinqCent = list(dic.keys())[list(dic.values()).index(100)] + list(dic.keys())[list(dic.values()).index(500)]
        liRoman.append(cinqCent)
        num -= 400
        print("JE SUIS LA :", num)

    if (num // 100 < 4):
        res = num // 100
        cent = list(dic.keys())[list(dic.values()).index(100)] * res
        liRoman.append(cent)
        num -= 100 * res

    if (num // 50 == 1):
        cinquante = list(dic.keys())[list(dic.values()).index(50)]
        liRoman.append(cinquante)
        num -= 50

    if (num // 40 == 1):
        quarante = list(dic.keys())[list(dic.values()).index(10)] + list(dic.keys())[list(dic.values()).index(50)]
        liRoman.append(quarante)
        num -= 40

    if (num // 10 < 4):
        res = num // 10
        # print(dic.get("X")*res)
        dizaines = list(dic.keys())[list(dic.values()).index(10)] * res
        liRoman.append(dizaines)
        num -= 10 * res

    if (num // 9 == 1):
        neuf = list(dic.keys())[list(dic.values()).index(1)] + list(dic.keys())[list(dic.values()).index(10)]
        liRoman.append(neuf)
        num -= 9

    print("ici", num // 5)

    if (num // 5 == 1):
        cinq = list(dic.keys())[list(dic.values()).index(5)]
        liRoman.append(cinq)
        num -= 5

    if (num // 4 == 1):
        quatre = list(dic.keys())[list(dic.values()).index(1)] + list(dic.keys())[list(dic.values()).index(5)]
        liRoman.append(quatre)
        num -= 4

    if (num // 1 < 4):
        res = num // 1
        unit = list(dic.keys())[list(dic.values()).index(1)] * res
        liRoman.append(unit)
        num -= 1 * res

    resultat = "".join(liRoman)

    print(resultat)

    return resultat


# to_roman(18)
# to_roman(19)
# to_roman(1464)
# to_roman(2025)
to_roman(3999)