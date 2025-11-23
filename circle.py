def circle(radius):
    for y in range(-radius, radius + 1):
        line = ""
        for x in range(-radius, radius + 1):
            if x*x + y*y <= radius*radius:
                line += "*"
            else:
                line += " "
        print(line)
