def golf_score(par, strokes):

    if(strokes==1):
        return "Hole in one!"
    else:
        match (par-strokes):
            case 0 :
                return "Par"
            case 1 :
                return "Birdie"
            case 2 :
                return "Eagle"
            case -1 :
                return "Bogey"
            case -2 :
                return "Double bogey"

print(golf_score(3, 3)) #Par
print(golf_score(4, 3)) #Birdie
print(golf_score(3, 1)) #Hole in one!
print(golf_score(5, 7)) #Double bogey
print(golf_score(4, 5)) #Bogey
print(golf_score(5, 3)) #Eagle