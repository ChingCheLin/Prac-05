COLORS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alizarin Crimson": "#e32636", "Apricot": "#fbceb1", "Arylide Yellow": "#e9d66b", "Baby Blue": "#89cff0", "Beaver": "#848482", "Bistre": "#3d2b1f", "Canary": "#ffff99", "Dark Sky Blue": "#8cbed6"}

color_code = input("Enter color name: ")

while color_code != "":
    if color_code in COLORS:
        print(color_code, "is", COLORS[color_code])
    else:
        print("Invalid color name")
    color_code = input("Enter color name: ")