def main():
    thought = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if thought == "42" or thought == "forty-two" or thought == "forty two":
        print("Yes")
    else:
        print("No")

main()
