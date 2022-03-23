import colorgram

colors = colorgram.extract('hirst.png', 30)
rgb_colors = []

for color in colors:
    r, g, b = color.rgb
    rgb_colors.append(
        (r, g, b)
    )

print(rgb_colors)

