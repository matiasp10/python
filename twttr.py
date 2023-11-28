def main():
    # Given an input text it is traversed,
    # if it is a vowel it is ignored,
    # otherwise it is passed to an auxiliary variable that will be printed as the output.
    text = input("Input: ")
    output = ""
    for c in text:
        if c == "o" or c == "O" or c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "u" or c == "U":
            output = output
        else:
            output = output + c
    print("Output:", output)
main()
