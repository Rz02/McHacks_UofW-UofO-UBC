from flask import Flask, render_template, request, jsonify
from cohere.classify import Example
import random
# Import CoHere and its API-KEY
import cohere
co = cohere.Client("N2ncDdn4Tz4Veh5x9nMeF3YcnY4BlCmqF45SsGoZ")

# Read CSV File
import pandas as pd
data = pd.read_csv("archive/recipes.csv")


recipe_name = data["recipe_name"]
ingredients = data['ingredients']
cuisine_level = data['rating']
preparation_time = data["total_time"]

#print(cuisine_level)
#print(ingredients)
#print(preparation_time)

time_list = [[int(s) for s in str(st).split() 
            if s.isdigit()] for st in preparation_time]

#print(time_list)

time_ints = [60*sublist[0] + sublist[1] if len(sublist) > 1 
             else sublist[0] if len(sublist) > 0
             else 0 for sublist in time_list]

time = pd.Series(time_ints)
data['total_time'] = time

# for time in time_ints:
#     if 'hrs' in time:
#         prepare_time = [60 * time[0] + time[1]]
#     else:
#         prepare_time = time[0]

# for time in range(len(preparation_time)):
#     if 'hrs' in time:
#         time_parts = time.split()
#         hours = int(time[0])
#         minutes = int(time[2])
#         total = hours * 60 + minutes
#     else:
#         time_parts = time.split()
#         mins = int(time[0])
#         total = mins

# Self Build Specific Food List
meat_related = ['tender', 'steak','brisket', 'chicken', 'beef', 'pork', 
                'mince', 'sausage', 'ham', 'fish', 'honey', 'milk', 'hot dog',
                'cheese', 'drumstick                                                                                                                    `````   ', 'egg', 'protein', 'fat', 'goose', 'lunch meat',
                'duck', 'quail', 'seafood', 'yogurt', 'butter', 'cream',
                'gelatine', 'dairy', 'bacon', 'elastin', 'collagen', 'aspic']

lactose_related = ['milk', 'yogurt', 'cheese', 'cream', 'lactose', 'whey', 
                   'bread', 'biscuit', 'cookie', 'cake', 'cereal', 'bacon',
                   'sausage', 'hot dog', 'lunch meat']

# Specific dataset rename
# non_vegan = [ing for ing in ingredients if any(ingr in ing for ingr in meat_related)]
vegan = [ing for ing in ingredients if not any(ingr in ing for ingr in meat_related)]
# lacto = [ing for ing in ingredients if any(ingr in ing for ingr in lactose_related)]
non_lacto = [ing for ing in ingredients if not any(ingr in ing for ingr in lactose_related)]

bad_recipe = data[cuisine_level < 4.5]
good_recipe = data[cuisine_level >= 4.5]

long_prep = data[time > 15]
short_prep = data[time <= 15]

# List Up Examples for Cultivation
examples = [
    # Choosing based on dietary 
    Example("I don't eat meat", random.choice(vegan)),
    Example("A dinner for vegan", random.choice(vegan)),
    Example("I don't dare to eat corn", random.choice(non_lacto)),
    Example("A dinner for lactose intolerance", random.choice(non_lacto)),

    # Choosing based on time
    Example("I am in rush", short_prep.sample()),
    Example("I don't want to put too much effort on cooking", short_prep.sample()),
    Example("I would like to enjoy cooking", long_prep.sample()),
    Example("I want to stay in the kitchen all day long", long_prep.sample()),

    # Choosing based on quality
    Example("I just need something to eat", bad_recipe.sample()),
    Example("An eatable dish is good enough", bad_recipe.sample()),
    Example("I'm craving something delicious", good_recipe.sample()),
    Example("I want to become a good chef", good_recipe.sample())
]

# inputs = [
#     "I want to be skinny",
#     "I have no appetite"
# ]

# response = co.classify(
#     model = 'large',
#     inputs = inputs,
#     examples = examples
# )

# print(response.classifications)

app = Flask(__name__)

@app.route('/chatbot', method = ['POST'])
def chatbot():
    message = request.json['message']
    response = cohere.generate_response(prompt = message)
    return jsonify(response)