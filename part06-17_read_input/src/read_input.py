# Write your solution here
def read_input(prompt: str, lower: int, upper: int):
    while True:
        try:
            entry = input(prompt)
            number = int(entry)
            if lower <= number <= upper:
                return number
            else:
                print(
                    f"You must type in an integer between {lower} and {upper} ", end=""
                )
        except ValueError:
            print(f"You must type in an integer between {lower} and {upper} ", end="")
