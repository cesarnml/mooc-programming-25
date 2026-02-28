def balanced_brackets(my_string: str):
    # Filter only bracket characters
    brackets = "".join(char for char in my_string if char in "()[]")

    # Base case: empty string is balanced
    if len(brackets) == 0:
        return True

    # If odd number of brackets, cannot be balanced
    if len(brackets) % 2 != 0:
        return False

    # Check if first and last brackets match
    matching = {"(": ")", "[": "]"}
    if brackets[0] not in matching or matching[brackets[0]] != brackets[-1]:
        return False

    # Recursively check the inner string
    return balanced_brackets(brackets[1:-1])
