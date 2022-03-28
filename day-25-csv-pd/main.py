import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data.columns)

fur_colors = squirrel_data["Primary Fur Color"]
print(fur_colors.unique())
color2num = {
    "Fur Color": [],
    "Number": []
}

for color in ["Gray", "Cinnamon", "Black"]:
    count = (fur_colors == color).sum()
    color2num["Fur Color"].append(color)
    color2num["Number"].append(count)

pd.DataFrame(color2num).to_csv("squirrel_count.csv")