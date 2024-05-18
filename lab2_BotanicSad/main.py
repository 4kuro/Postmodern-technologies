import sys
#variant 1(16)
def calculate(expression):
    expression = expression.replace(" ", "")
    if not is_valid_brackets(expression):
        raise ValueError("Invalid expression: incorrect bracket usage")
    is_valid_symbol(expression)

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error in calculation: {e}")

def is_valid_brackets(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # Unmatched closing bracket
            stack.pop()

    return len(stack) == 0  # Return True if all brackets are matched

def is_valid_symbol(expression):
    allowed_symbols = "0123456789+-*/() "
    for char in expression:
        if char not in allowed_symbols:
            raise ValueError("Invalid expression: contains disallowed characters")

def main():
    try:
        expression = sys.stdin.readline().strip()
        result = calculate(expression)
        sys.stdout.write(result + "\n")
        sys.exit(0)
    except ValueError as ve:
        sys.stderr.write(str(ve) + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
