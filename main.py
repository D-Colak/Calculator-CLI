def main():
    inp: str = input(
        "Enter your math expression in the format: number operation number. Valid operations are +, -, *, /, ^, and MOD. Example: 5 + 3\n"
        "Note: Use spaces between the numbers and the operation.\n"
    )
    arr: list[str] = inp.split()
    if len(arr) != 3:
        print("Invalid input. Please enter in the format: number operation number")
        return

    try:
        n1: int = int(arr[0])
        n2: int = int(arr[2])
    except ValueError:
        print("Invalid input. Please ensure both numbers are valid integers.")
        return

    o: str = arr[1]
    res: float = 0.0

    if o == "+":
        res = n1 + n2
    elif o == "-":
        res = n1 - n2
    elif o == "*":
        res = n1 * n2
    elif o == "/":
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        res = n1 / n2
    elif o == "^":
        res = n1**n2
    elif o == "MOD":
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        res = n1 % n2
    else:
        print("Invalid operation. Valid operations are +, -, *, /, ^, and MOD.")
        return

    print(f"{inp} = {res}")


if __name__ == "__main__":
    main()
