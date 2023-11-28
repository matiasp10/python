def main():
    convert(input())

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text)

main()
