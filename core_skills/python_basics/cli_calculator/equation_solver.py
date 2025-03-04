from helpers.equation_parser import parse_equation

def solve_linear(a, b, c):
    """Solve a*x + b = c for x."""
    if a == 0:
        return "Error: Coefficient 'a' cannot be zero."
    return (c - b) / a

def cli_calculator():
    print("Welcome to the enhanced CLI Calculator!")
    while True:
        user_input = input("Enter a linear equation (e.g., 2x+3=7) or type 'exit' to quit: ")
        if user_input.lower() == "exit":
            break
        try:
            a, b, c = parse_equation(user_input)
            result = solve_linear(a, b, c)
            print(f"Solution: x = {result}")
        except ValueError as err:
            print(err)
    print("Goodbye!")

if __name__ == "__main__":
    cli_calculator()
