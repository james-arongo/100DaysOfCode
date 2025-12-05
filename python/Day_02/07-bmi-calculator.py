# Calculates a person's body mass index using the Metric formula
weight = float(input("Enter your weight (kg): \n>"))
height = float(input("Enter your height (m): \n>"))

bmi = weight / height ** 2
print(bmi)

