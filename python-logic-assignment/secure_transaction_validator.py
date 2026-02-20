balance = int(input("Balance: "))
withdrawal = int(input("Withdrawal: "))
verified = input("Verified: ")

if verified == "True" and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
