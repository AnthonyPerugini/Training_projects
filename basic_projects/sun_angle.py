def sun_angle(time):
    hh = int(time.split(":")[0])
    mm = int(time.split(":")[1])
    total_minutes = (hh * 60) + mm
    if total_minutes > 1080 or total_minutes < 360:
        return "I don't see the sun!"
    else:
        return float((total_minutes - 360) / 4)

