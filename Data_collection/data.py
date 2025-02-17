import pandas as pd

og_link = "https://www.thecocktaildb.com"
drinks = pd.read_csv("drinks.csv")
ingredients = pd.read_csv("ingredients.csv")

# print(drinks[10:20]['name'])
