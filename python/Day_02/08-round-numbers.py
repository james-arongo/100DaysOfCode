# This program uses the round() function to round a number to a certain number of decimal points of accuracy. This rounds off the bmi calculator to two decimal places.
weight = float(input("Enter your weight (kg): \n>"))
height = float(input("Enter your height (m): \n>"))

bmi = weight / height ** 2
print(round(bmi, 2))

