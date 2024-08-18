# python Calc using a match case instead of if


operator = input("Enter a Operator + - * /: ")
numb_1 = float(input("Enter the first number: "))
numb_2 = float(input("Enter the second number: "))
numb_3 = float(input("Enter the third number: "))



match operator:
    case "+":
        result = numb_1 + numb_2 + numb_3
        print(round(result, 3))
    case "-":
        result = numb_1 - numb_2 - numb_3
        print(round(result, 3))
    case "*":
        result = numb_1 * numb_2 * numb_3
        print(round(result, 3))
    case "/":
        result = numb_1 / numb_2 / numb_3
        print(round(result, 3))
        # this is the else for match case
    case _:
        print(f'{operator} is not a vaild operator')


