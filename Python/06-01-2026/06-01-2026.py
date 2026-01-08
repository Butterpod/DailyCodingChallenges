def vowel_case(s):
    vowel=["a","e","i","o","u"]

    strRes=""

    for i in s:
        if (i.lower() in vowel):
            strRes+=i.upper()
        else:
            strRes+=i.lower()
    print(strRes)
    return strRes

vowel_case("vowelcase") # "vOwElcAsE".
vowel_case("coding is fun") # "cOdIng Is fUn"
vowel_case("HELLO, world!") # "hEllO, wOrld!"
vowel_case("git cherry-pick") # "gIt chErry-pIck".
vowel_case("HEAD~1") # "hEAd~1"