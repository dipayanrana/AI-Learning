def solve_linear(a, b, c):
    """
    Solve a linear equation of the form: a*x + b = c.
    Returns the solution for x.
    """
    try:
        return (c - b) / a
    except ZeroDivisionError:
        return "Error: Coefficient 'a' cannot be zero."

# Example: Solve 2x + 3 = 7
if __name__ == "__main__":
    a = 2
    b = 3
    c = 7
    x = solve_linear(a, b, c)
    print(f"Solution for the equation 2x+3=7 is: x = {x}")
