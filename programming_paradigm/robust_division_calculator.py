def safe_divide(numerator, denominator):
    """
    Perform division with error handling for zero division and non-numeric inputs.
    :param numerator: The numerator for division (expected to be convertible to float).
    :param denominator: The denominator for division (expected to be convertible to float).
    :return: The result of the division or an appropriate error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."
