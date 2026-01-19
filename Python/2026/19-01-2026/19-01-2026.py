def compare_energy(calories_burned, watt_hours_used):
    cal_joul = 4184
    watth_joul = 3600

    if (calories_burned * 4184 > watt_hours_used * 3600):
        return "Workout"
    elif (calories_burned * 4184 < watt_hours_used * 3600):
        return "Devices"
    else:
        return "Equal"


compare_energy(250, 50)  # "Workout"
compare_energy(100, 200)  # "Devices".
compare_energy(450, 523)  # "Equal".
compare_energy(300, 75)  # Workout"
compare_energy(200, 250)  # "Devices"
compare_energy(900, 1046)  # "Equal"