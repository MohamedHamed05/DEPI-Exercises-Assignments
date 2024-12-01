import calc

while True:
    cmd = input("Enter command (add, sub, mult, div) or 'stop' to exit: ").lower()
    if cmd == "stop":
        print("Exiting...")
        break

    if cmd in ["add", "sub", "mult", "div"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if cmd == "add":
                result = calc.add(num1, num2)
            elif cmd == "sub":
                result = calc.sub(num1, num2)
            elif cmd == "mult":
                result = calc.mult(num1, num2)
            elif cmd == "div":
                result = calc.div(num1, num2)

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid command. Try again.")
