# Python Calculator.
#BroCode https://youtu.be/4wGuB3oAKc4?si=ZGdoU7UFO80AGcKU


# user to select a arthimetic operator
operator = input("Enter a operator (+ - * /): ")

# create a var for the first and second number
# this forms string concatenation
# numb1 = input("Enter First number: ")
# numb2 = input("Enter Second number: ")

# print(numb1 + numb2) # string concatenation just join two strings together

# comes up with 1011
# accepting user input there accepted as sting data imports

# test print with just
# num1 + num2
numb1 = float(input("Enter First number: "))
numb2 = float(input("Enter Second number: "))

# print(numb1 + numb2)
# this was for a test

# using if statements to check weather user is using different operators
# inside we placed a result var for the results of each operator
if operator == "+":
    result = numb1 + numb2
    print(result)
elif operator == "-":
    result = numb1 - numb2
    print(result)
elif operator == "*":
    result = numb1 * numb2
    print(result)
elif operator == "/":
    result = numb1 / numb2
    print(result)
else:
    print("please use one of the following operators + - * /")


