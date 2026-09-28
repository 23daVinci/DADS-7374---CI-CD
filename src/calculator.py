def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Calculator")
    print("Supported operations: +, -, *, /")

    while True:
        expression = input("Enter expression (e.g. 3 + 4), or 'q' to quit: ").strip()
        if expression.lower() == "q":
            break

        parts = expression.split()
        if len(parts) != 3 or parts[1] not in operations:
            print("Invalid input. Use format: <number> <operator> <number>")
            continue

        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            result = operations[op](a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
