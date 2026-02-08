def calculate_penalty_distance(rounds):
    res=0
    for i in rounds:
        a=5-i
        res+=a*150
    print("resultat: ",res)

    return res

calculate_penalty_distance([4, 4]) #300.
calculate_penalty_distance([5, 5]) # 0
calculate_penalty_distance([4, 5, 3, 5])# 450
calculate_penalty_distance([5, 4, 5, 5]) # 150
calculate_penalty_distance([4, 3, 0, 3])#1500