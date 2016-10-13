import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def ask():
  answers = dict()
  for k,q in questions.items():
    a = raw_input(q)
    answers[k] = True if a[0] == 'y' else False
  return answers
    
def makedrink(answers):
  drink = []
  for k,v in answers.items():
    if v:
      drink.append(random.choice(ingredients[k]))
  return drink

if __name__ == '__main__':
  answers = ask()
  drink = makedrink(answers)
  print drink