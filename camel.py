def main():
    name = input("camelCase: ")
    result = ""
    for c in name:
        if c == c.lower():
            result = result + c
        else:
            result = result + "_" + c.lower()
    print("snake_case:", result)

main()
