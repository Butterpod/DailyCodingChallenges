def format_date(date_string):
    newStri = date_string.replace(",", "")
    liDate = newStri.split()

    year = 0

    liResult = []
    result = ""
    match liDate[0]:


        case "January":
            month = "01"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "February":
            month = "02"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "Mars":
            month = "03"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "April":
            month = "04"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "May":
            month = "05"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "June":
            month = "06"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "July":
            month = "07"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "August":
            month = "08"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "September":
            month = "09"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "October":
            month = "10"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "November":
            month = "11"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

        case "December":
            month = "12"
            if (len(liDate[1]) < 2):
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append("0" + liDate[1])
            else:
                liResult.append(liDate[2])
                liResult.append(month)
                liResult.append(liDate[1])

    print("JUIL A")
    result = "-".join(liResult)
    print(result)

    return result

format_date("December 6, 2025")
format_date("January 1, 2000")
format_date("November 11, 1111")