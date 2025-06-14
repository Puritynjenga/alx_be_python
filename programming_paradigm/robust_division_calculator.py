def safe_divide(numerator,denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        result = (num1 / num2)

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return result
    
     