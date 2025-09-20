def main():
    while True:
        calc = input("Enter an expression like: <number> <operator> <number>\n"
                     "Example: 2.5 * 4 \n> ").strip()

        if "," in calc:
            print("Error: use a dot for the decimal part, not a comma.")
            continue

        parts = calc.split()
        if len(parts) != 3:
            print("Error: the expression must be in the format: <number> <operator> <number>")
            continue

        left, op, right = parts

        if op not in correct_oper:
            print(f"Error: operator '{op}' is not supported. Available: {', '.join(correct_oper)}")
            continue

        try:
            x = parse_number(left)
            y = parse_number(right)
        except ValueError:
            print("Error: invalid number. Use integers or real values.")
            continue

        try:
            if op == "+":
                res = add(x, y)
            elif op == "-":
                res = sub(x, y)
            elif op == "*":
                res = mul(x, y)
            elif op == "/":
                res = div(x, y)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        print("Result:", res)

if __name__ == "__main__":
    main()