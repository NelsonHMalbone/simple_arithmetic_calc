# python Calc using a match case instead of if


operator = input("Enter a Operator + - * / or 'Quit' to exit: ")
numb_1 = float(input("Enter the first number: "))
numb_2 = float(input("Enter the second number: "))



while True:
    try:
        match operator:
            case "Quit":
                print("Exiting the program")
                break
            case "+":
                result = numb_1 + numb_2
                print(round(result, 3))
            case "-":
                result = numb_1 - numb_2
                print(round(result, 3))
            case "*":
                result = numb_1 * numb_2
                print(round(result, 3))
            case "/":
                try:
                    result = numb_1 / numb_2
                    print(round(result, 3))
                    # this is the else for match case
                except ZeroDivisionError:
                    print("Error: Division by zero is not")
                    break
            case _:
                print(f'{operator} is not a vaild operator')
    except TypeError:
        print("Error: Invalid input types.")

