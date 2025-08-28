bids = {}
betting = True
print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________
                    """)

print("Welcome to the secret auction program")

while betting:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))

    bids[name] = bid

    status = input("Does anyone else need to bet? Type 'y' for yes, or 'n' for no: ")

    if status == 'n':
        betting = False
    else:
        print("\n"*100)

max_bid = 0.0
current_winner = ""

for person in bids:
    current_bid = bids[person]
    if current_bid >= max_bid:
        max_bid = current_bid
        current_winner = person

print("\n"*100)
print(f"The winner is {current_winner} with a bid of ${max_bid}")


    