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

def asking_questions(questions):
#asking questions and creating a new dictionary
    answers = {}
    for item in questions:
        while True:
            answer = input(questions[item] + "\nyes/no: ")
            if answer == "yes":
                answer = True
                break
            elif answer == "no":
                answer = False
                break
            else:
                answer = input("Enter a valid answer, please..." + "\nyes/no: ")
        answers[item] = answer
    return answers

def mixing_drinks(answers):
#mixing a drink
    drink = []
    for item in set(answers) & set(ingredients):
        if answers[item] == True:
            drink.append(random.choice(ingredients[item]))
    return drink

if __name__ == '__main__':
    answers = asking_questions(questions)
    drink = mixing_drinks(answers)
    print("Ingredients:", ", ".join(drink))