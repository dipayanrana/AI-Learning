def parse_equation(equation_str):
    """
    Parse a simple linear equation of the form 'ax+b=c'
    and return (a, b, c) as floats.
    Note: This example expects no spaces and a single variable 'x'.
    """
    try:
        left, right = equation_str.split('=')
        c = float(right)
        # Find the position of 'x'
        x_index = left.find('x')
        a = float(left[:x_index]) if left[:x_index] not in ["", "+"] else 1.0
        # Extract b by removing the coefficient and 'x'
        b_str = left[x_index+1:]
        b = float(b_str) if b_str != "" else 0.0
        return a, b, c
    except Exception as e:
        raise ValueError(f"Invalid equation format: {equation_str}") from e
