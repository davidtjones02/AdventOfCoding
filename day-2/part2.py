position = {"horizontal": 0, "aim": 0, "depth": 0}


with open("commands.txt", "r") as file:
    # read each line and see if it contains horizontal or depth
    for line in file:
        if "forward" in line:
            position["horizontal"] += int(line.split()[1])
            position["depth"] += int(line.split()[1]) * position["aim"]
        elif "up" in line:
            position["aim"] -= int(line.split()[1])
        else:
            position["aim"] += int(line.split()[1])


# multiply position horiziontal with position depth
print(position["horizontal"] * position["depth"])
