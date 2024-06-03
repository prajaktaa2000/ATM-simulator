
while True:
    print(" ***** Welcome To ATM Machine Simulator ***** ")
    pin = int(input("Enter your pin: "))

    acc_bal = 10000


    def check_balance():
        return f"Account balance: ₹{acc_bal}"

    def withdraw():
        global acc_bal
        amount = int(input("Enter amount to withdraw: "))
        if amount > acc_bal:
            return "Balance is low"
        else:
            acc_bal = acc_bal - amount
            return f"₹{amount} debited successfully, updated account balance is ₹{acc_bal}"


    def deposit():
        global acc_bal
        amount = int(input("Enter amount to deposit: "))
        acc_bal = acc_bal + amount
        return f"₹{amount} credited successfully, updated account balance is ₹{acc_bal}"



    if pin == 6556:
        while True:
            print("\nSelect Your Transaction from the above options: ")
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print(check_balance())
            elif choice == "2":
                print(withdraw())
            elif choice == "3":
                print(deposit())
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid pin")






