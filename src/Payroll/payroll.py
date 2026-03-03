import csv

def read_data(file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            data = [row for row in csv_reader]
        return data

input_data = read_data('input.data')

class payroll:

    for read_data in input_data:
        print(read_data)
        employee_id = read_data[0]
        hours_worked = float(read_data[1])
        hourly_rate = float(read_data[2])
        gross_pay = hours_worked * hourly_rate
        print(f"Employee ID: {employee_id}, Gross Pay: ${gross_pay:.2f}")

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_gross_pay(self):
        return self.hours_worked * self.hourly_rate
    
    def calculate_net_pay(self, tax_rate):
        gross_pay = self.calculate_gross_pay()
        tax_amount = gross_pay * tax_rate
        net_pay = gross_pay - tax_amount
        return net_pay
    
    def calculate_tax_amount(self, tax_rate):
        gross_pay = self.calculate_gross_pay()
        tax_amount = gross_pay * tax_rate
        return tax_amount
    
    def display_payroll_info(self, employee_id, tax_rate):
        gross_pay = self.calculate_gross_pay()
        net_pay = self.calculate_net_pay(tax_rate)
        print(f"Employee ID: {employee_id}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print(f"Tax Amount: ${self.calculate_tax_amount(tax_rate):.2f}")
    
    
