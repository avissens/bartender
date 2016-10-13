import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def asking_questions(x):
   answers = {}
   for item in x:
       answer = 'dummy'
       while answer.lower() not in ['yes', 'no']:
           answer = input(questions[item] + "\nyes/no: ")
           if answer.lower() not in ['yes', 'no']:
               print('Please enter [yes] or [no]')
       answers[item] = answer
   return answers

def mixing_drinks(x):
#mixing a drink
    drink = []
    answers = asking_questions(questions)
    for item in set(answers) & set(ingredients):
        if answers[item] == True:
            drink.append(random.choice(ingredients[item]))
    print("Ingredients:", ", ".join(drink))
print(mixing_drinks(ingredients))

    