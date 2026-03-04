import csv

with open('input.data', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    input_data = [row for row in csv_reader]
    
def read_data(input_data):
    with open(input_data, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
        return data
    
input_data = read_data('input.data')

balance = 0.0
for row in input_data:
    transaction_type = row[1].strip().lower()
    amount = float(row[2])

    if transaction_type == 'deposit':
        balance += amount
    elif transaction_type == 'withdrawal':
        balance -= amount

print(f"Final Balance: ${balance:.2f}")
