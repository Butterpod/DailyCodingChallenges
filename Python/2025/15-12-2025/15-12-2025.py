def speed_check(speed_mph, speed_limit_kph):

    speed_km=speed_mph*1.60934

    print(speed_km)

    if (speed_km<=speed_limit_kph):
        print("Not Speeding")
        return "Not Speeding"
    elif (speed_km<=speed_limit_kph+5):
        print("Warning")
        return "Warning"
    else:
        print("Ticket")
        return "Ticket"



speed_check(30, 70) #"Not Speeding".
speed_check(40, 60) #"Warning"
speed_check(40, 65) #"Not Speeding".

speed_check(60, 90) #"Ticket"
speed_check(65, 100) #"Warning"


speed_check(88, 40) #"Ticket"