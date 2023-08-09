import time as s


acc_pin = 1111
acc_balance = 100000
user_name = "user"
print("Welcome to ABC bank account", user_name, end = "\n")

user_inp = 9

while (True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change PIN")
    print("\t\t5. Return Card")
    user_inp = int(input("Please select a number to proceed  "))
    print("\n\n")

    if user_inp == 0:
        print("You have been logged out. Thank you!\n\n")
        break

    elif user_inp in (1,2,3,4,5):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == acc_pin:
                print("Welcome\n\n")

                if user_inp == 1:
                    print("Processing Account balance...")
                    s.sleep(1)
                    print("Your account balance is Rs.", acc_balance, end = "\n\n\n")
                    break
                elif user_inp == 2:
                    print("Processing Cash Withdrawl")
                    s.sleep(1)

                    while(True):
                        withdrawl_amount = float(input("Please enter the amount you want to withdraw  "))

                        if withdrawl_amount > acc_balance:
                            print("Can't withdraw Rs.", withdrawl_amount)
                            print("Your account has not sufficient amount, please enter a lower amount")
                            continue

                        else:
                            print("Withdrawing Rs.", withdrawl_amount)
                            confirm = input("Confirm? Y/N  ")
                            if confirm in ('Y', 'y'):
                                acc_balance -= withdrawl_amount
                                print("Amount withdrawn - Rs.", withdrawl_amount)
                                print("Remaining balance - Rs.", acc_balance, end = "\n\n")
                                break

                            else:
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif user_inp == 3:
                    print("Processing Cash Deposit...")
                    s.sleep(1)

                    deposit_amount = float(input("Please enter the amount you wish to deposit  "))
                    print("Depositing Rs.", deposit_amount)
                    confirm = input("Confirm? Y/N  ")
                    if confirm in ('Y', 'y'):
                        acc_balance += deposit_amount
                        print("Amount deposited - Rs.", deposit_amount)
                        print("Updated available balance - Rs.", acc_balance, end = "\n\n\n")
                    else:
                        print("Transaction Cancelled!\n\n")

                    break


                elif user_inp == 4:
                    print("Processing PIN Change...")
                    s.sleep(1)

                    new_pin = int(input("Please enter your new PIN  "))

                    print("PIN changed -", new_pin)
                    confirm = input("Confirm? Y/N  ")
                    if confirm in ('Y', 'y'):
                        acc_pin = new_pin
                        print("PIN changed successfully! \n\n")
                    else:
                        print("Process Cancelled!\n\n")

                    break

                else:
                    print("Processing Card Return...")
                    s.sleep(2)

                    print("Do yu want to remove your card")
                    confirm = input("Confirm? Y/N  ")
                    if confirm in ('Y', 'y'):
                        print("Card returned successfully! \n\n")
                    else:
                        print("Process Cancelled!\n\n")

                    break

            else:
                num_of_tries -= 1
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n\n")

        else:
            print("You have been logged out Successfully !!!. Thank you for using ABC Atm!\n\n")
            break


    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        continue
