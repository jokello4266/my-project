# Variables 
name="Walter"
print(name)
name="Angela"
print(name)

# Print statements
print(str(70) + str(100))
print(70 + 100)

# inputs
name=input("what is your name ?")
num_char = len(name)
new_num_char = str(num_char)
a=float(123)
print(a)
print("Your name has " + new_num_char + "" + " characters")

# Data-type exercise 2 
# Adding intergers 
two_digit_number = input("Please enter 2 numbers you would like to add ")
first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print("The sum of the 2 numbers you inputed is ",two_digit_number)

# BMI Calculation
weight_pounds=input("What is your weight m ?")
weight_kg=weight_pounds/2.205

height_ft=input("What is your height in kg ?")
height_inches= height_ft * 12

weight_as_float = float(weight_kg)
height_as_float = float(height_inches)

BMI= height_as_float // weight_as_float

if BMI in range(25, 29.9):
    print("You are overweight")
else:
    BMI > 30
    print("You are obese")






