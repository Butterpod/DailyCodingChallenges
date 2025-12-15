def title_case(title):
    li_split = title.split()
    li_res = []

    for i in li_split:
        li_res.append(i.capitalize())

    res = " ".join(li_res)

    return res


title_case("hello world")  # "Hello World".
title_case("the quick brown fox")  # "The Quick Brown Fox"
title_case("JAVASCRIPT AND PYTHON")  # "Javascript And Python"
title_case("AvOcAdO tOAst fOr brEAkfAst")  # "Avocado Toast For Breakfast"
