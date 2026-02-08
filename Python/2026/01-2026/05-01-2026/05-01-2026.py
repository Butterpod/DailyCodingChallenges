def convert(val, range_b):
    if (val / 14.5038 > range_b[1]):
        return "High"
    elif (val / 14.5038 < range_b[0]):
        return "Low"
    else:
        return "Good"


def tire_status(pressures_psi, range_bar):
    listRes = []

    for i in pressures_psi:
        listRes.append(convert(i, range_bar))

    print(listRes)

    return listRes


tire_status([32, 28, 35, 29], [2, 3])
tire_status([32, 28, 35, 30], [2, 2.3])
tire_status([29, 26, 31, 28], [2.1, 2.5])
tire_status([31, 31, 30, 29], [1.5, 2])
tire_status([30, 28, 30, 29], [1.9, 2.1])
