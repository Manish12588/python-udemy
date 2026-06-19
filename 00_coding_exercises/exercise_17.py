"""
ATM Withdrawal Simulator
Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session.
Your task is to simulate how the system should handle each request based on the account balance.
Tasks:
Use a while loop to iterate through the list named withdrawals.

For every withdrawal:
✅ If the current balance is enough:
Subtract the amount.
Append a success message: "Withdrawn: {amount}"
❌ If not enough:
Append a message: "Insufficient funds for requested amount: {amount}"
After all withdrawals:
Append the final balance as: "Remaining Balance: balance"
Return a list containing all the messages.
"""

result = []
index = 0

balance = 10000
withdrawals = [1000, 2000, 3000, 4000, 1000]

while index < len(withdrawals):
    amount = withdrawals[index]
    if amount <= balance:
        balance -= amount
        result.append(f"withdrawn: {amount}")
    else:
        print(f"Insufficient funds for requested amount: {amount}")
    index += 1
result.append(f"Remaining Balance: {balance}")
print(f"Final Results: {result}")
