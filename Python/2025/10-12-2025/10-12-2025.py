import re


def parse_bold(markdown):
    # print(markdown.split())
    liSplit = markdown.split()

    liResult = []
    if "**" in liSplit or "__" in liSplit:
        return markdown

    for i in liSplit:

        # Catch les "**"
        if i.startswith("**") and i.endswith("**"):
            rep1 = i.replace("**", "")
            rep2 = "<b>" + rep1 + "</b>"
            liResult.append(rep2)


        elif i.startswith("**"):
            liResult.append(i.replace("**", "<b>"))

        elif i.endswith("**"):
            liResult.append(i.replace("**", "</b>"))

        ## catch les "__"
        elif i.startswith("__") and i.endswith("__"):
            rep1 = i.replace("__", "")
            rep2 = "<b>" + rep1 + "</b>"
            liResult.append(rep2)

        elif i.startswith("__"):
            liResult.append(i.replace("__", "<b>"))

        elif i.endswith("__"):
            liResult.append(i.replace("__", "</b>"))

        else:
            liResult.append(i)

    # print(liResult)
    result = " ".join(liResult)
    print(result)
    return result


parse_bold("**This is bold**")
# parse_bold("__This is also bold__")
# parse_bold("__This is also bold__")
# parse_bold("**This is not bold **")
# parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")
"""
if "**" in i and len(i)>2:
            if i.startswith("**"):
                liResult.append(i.replace("**","<b>"))
            if i.endswith("**"):
                liResult.append(i.replace("**","</b>"))
        else:
            liResult.append(i)
"""
# print(liResult)

