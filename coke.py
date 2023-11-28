def main():
    # as long as the amount of money is less than 50 cents,
    # ask to enter valid coins, once they are completed or exceeded 50 cents,
    # the available change is displayed.
    amount = 0
    while amount < 50:
        print("Amount Due:", 50 - amount)
        money = int(input("Insert Coin: "))
        if money == 5 or money == 10 or money == 25:
            amount = amount + money

    print("Change Owed:", amount - 50)

main()
