def to_consonant_case(s):
    vowel = ["a", "e", "i", "o", "u"]

    strRes = ""

    for i in s:
        if (i.lower() in vowel):
            i.replace("-", "_")
            strRes += i.lower()
        else:
            i.replace("-", "_")
            strRes += i.upper()

    return strRes.replace("-", "_")


to_consonant_case("helloworld")  # "HeLLoWoRLD"
to_consonant_case("HELLOWORLD")  # "HeLLoWoRLD"
to_consonant_case("_hElLO-WOrlD-")  # "_HeLLo_WoRLD_"
to_consonant_case("_~-generic_~-variable_~-name_~-here-~_")  # "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_"