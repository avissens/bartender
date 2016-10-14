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

#lists of names and adjectives for random drinks
drink_noun = ["Margo", "Ice", "Dog", "Bird", "Heart"]
drink_adjective = ["Fluffy", "Bloody", "Sunny", "Yellow", "Blue"]

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

def main():
#main function asking questions and mixing drinks
    answers = asking_questions(questions)
    drink = mixing_drinks(answers)
    print("Ingredients:", ", ".join(drink))
    print(random.choice(drink_adjective) + " " + random.choice(drink_noun) + " " + "it is!")

if __name__ == '__main__':
    main()

#asking for another drink
    while True:
        customer = input("Would you like another drink?" + "\nyes/no: ")
        if customer == "yes":
            main()
        elif customer == "no":
            print("Enjoy yourself and see you soon!")
            break
        else:
            print("Pardon, I didn't get it...")
            continue
