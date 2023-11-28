def main():
    speak = input()
    speak = speak.split(" ")
    print(*speak, sep="...")
main()
