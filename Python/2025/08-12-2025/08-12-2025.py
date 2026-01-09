def convert_to_kgs(lbs):
    lbsTokg = lbs * 0.453592
    convert = round(lbsTokg, 2)
    result = ""
    oneKg = "kilogram."
    oneLbs = "pound"

    # print("Value: %.2f" % float(convert))

    if (lbs == 1):
        result = str(lbs) + " " + oneLbs + " equals " + "%.2f" % convert + " kilograms."

    elif (convert == 1):
        result = str(lbs) + "" + " pounds" + " equals " + "%.2f" % convert + " " + oneKg

    else:
        result = str(lbs) + "" + " pounds" + " equals " + "%.2f" % convert + " kilograms."

    print(result)
    return result


convert_to_kgs(1)
convert_to_kgs(0)
convert_to_kgs(100)
convert_to_kgs(2.20462)