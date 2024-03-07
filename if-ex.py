import random
drinks = ["vodka", "tequila", "wiskey", "gin", "rum"]
try:
    name= input("what is your name? ")
    age = input("how old are you? ")
    age = int(age)
    country = input("Where are you from? ")
except:
    print("Invalid age.")
else:
    if age < 0 or age > 140:
        print("You are not human. This game is for humans only")
    elif age > 120:
        print("You are too old to play the awsome drinking game.")
    elif age < 18:
        print("You are a minor. You can not play this awsome drinking game.")
    elif country == "USA" or country == "UAE" and age < 21:
        print("You are not allowed to drink in your country. Thus you cannot play this awsome drinking game")
    else:
        print("You are an adult. You can not play this awsome drinking game.")
        print("have some", random.choice(drinks), "and enjoy the game.")
