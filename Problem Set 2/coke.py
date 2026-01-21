# simulates a coin-operated machine that accepts 50, 25, 10, and 5 cent coins until 50 cents is paid,
# then prints the change owed if overpaid.

def loop():
    due = 50
    while due >0:
        inserted = int(input("Insert Coin: "))
        if inserted in {50, 25, 10, 5}:
            due = due - inserted 
            if due > 0:
                print(f"Amount Due: {due}"  )
            else:
                print(f"Change Owed: {abs(due)}")

def main():
    loop()

main()  