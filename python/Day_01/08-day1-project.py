# This a CLI program that creates a band name by combining answers from two questions
print("Hello,", input("What is your name? "), "Welcome to the Band Name Generator!")
green = "\033[32m"
reset = "\033[0m"
city = input(green + "Which city did you grow up in?\n> ")
print(reset + "What's your pet's name?")
pet = input(green + "What is the name of your favorite pet?\n> ")
print(reset + "The name of your band could be: " + city + " " + pet)
