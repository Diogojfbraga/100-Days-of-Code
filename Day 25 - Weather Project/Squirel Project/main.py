import pandas as pd

data = pd.read_csv(
    "Day 25 - Weather Project/Squirel Project/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
) 


fur_colour = data["Primary Fur Color"].value_counts()

fur_colour.to_csv("Squirel_count.csv")

print(fur_colour)
