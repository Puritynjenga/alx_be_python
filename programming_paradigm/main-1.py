import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    if isinstance(result, str):
        # Print the error message directly if safe_divide returned a string error.
        print(result)
    else:
        print(f"The result of the division is {result:.1f}")

if __name__ == "__main__":
    main()