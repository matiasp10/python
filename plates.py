def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # I check if the license plate does not have between 2 and 6 characters,
    # if the first 2 are alphabetic characters and if the other characters are alphanumeric.
    if not 2 <= len(s) <= 6 or not s[0:2].isalpha() or not s[2:].isalnum():
        return False
    # by means of a loop, I will iterate the remaining characters of the license plate
    # and if it is a number I add it to a stack variable, I check if the first one is a 0,
    # and if it is not a number it means that there is an alphabetic character in between so it would also be false.
    stack = []
    for i in s[2:]:
        if i.isdigit():
            stack.append(i)
            if stack[0] == '0':
                return False

        elif stack and i.isalpha():
            return False

    return True

main()
