def get_average_grade(scores):
    dic={
        "A+":range(97,101),
        "A":range(93,97),
        "A-":range(90,93),
        "B+":range(87,90),
        "B":range(83,87),
        "B-":range(80,83),
        "C+":range(77,80),
        "C":range(73,77),
        "C-":range(70,73),
        "D+":range(67,70),
        "D":range(63,67),
        "D-":range(60,63),
        "F":range(0,60)
    }

    mean_val=sum(scores)//len(scores)
    #https://www.geeksforgeeks.org/python/python-get-key-from-value-in-dictionary/
    for key, val in dic.items():
        if mean_val in val:
            print(key)
            return key

get_average_grade([92, 91, 90, 94, 89, 93])#"A-".
get_average_grade([84, 89, 85, 100, 91, 88, 79])# "B+".
get_average_grade([63, 69, 65, 66, 71, 64, 65]) # "D"
get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100])#"A+".
get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]) # "C+".
get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]) #"F".