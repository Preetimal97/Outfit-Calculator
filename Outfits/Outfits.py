
import random

print ("Welcome to the outfit choosing machine")

while True:
    user_input = input("Type rainy, sunny, or snowy day ").lower()

    if user_input == "rainy":
        user_input = input("Type work, errands, home ").lower()
        if user_input == "work":
           print ("I suggest a pantsuit with waterproof ankle boots")
        if user_input == "errands":
           print ("I suggest a tracksuit and rain boots")
        if user_input == "home":
           print ("I suggest cozy sweats with fuzzy slippers")

    if user_input == "sunny":
        user_input = input("Type work, beach, party ").lower()
        if user_input == "work":
           print ("I suggest a cotton dress with open toed pumps")
        if user_input == "beach":
           print ("I suggest a tracksuit and rain boots")
        if user_input == "party":
           print ("I suggest a silk dress with glitter heels")

    if user_input == "snowy":
        user_input = input("Type work from home, sledding, home ").lower()
        if user_input == "work from home":
            print("I suggest a flannel shirt with leggings")
        if user_input == "sledding":
            print("I suggest a puffer jacket with slacks and snow boots")
        if user_input == "home":
            print("I suggest a wool sweater and sweatpants")