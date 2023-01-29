import pandas as pd

df = pd.read_csv('Ingredients.csv')


def query(recipe):
  query = (df['recipe_name'] == recipe)
  row = df[query].iloc[0]
  ingredients = row['ingredients']

  ingredients = url(ingredients)
  recipe = url(recipe)
  start = "https://www.nutritionix.com/q2?i="
  joint = "+&n="
  return start + ingredients + joint + recipe


def url(str):
  str = str.replace("'", '')
  str = str.replace("]", '')
  str = str.replace("[", '')
  str = str.replace("½", '1/2')
  str = str.replace("¾", '3/4')
  str = str.replace("¼", '1/4')
  str = str.split()
  return '%20'.join(str)
