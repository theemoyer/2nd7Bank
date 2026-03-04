import csv

with open('input.data', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    input_data = [row for row in csv_reader]

def read_data(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        return [row for row in csv_reader]

class payroll:

    for read_data in input_data:
        employee_id = read_data[0]
        hours_worked = float(read_data[1])
        hourly_rate = float(read_data[2])
        gross_pay = hours_worked * hourly_rate
        print(f"Name: {employee_id}\nHours Worked: {hours_worked}\nHourly Rate: ${hourly_rate:.2f}\nGross Pay: ${gross_pay:.2f}\nTax Amount: ${gross_pay * 0.2:.2f}\nNet Pay: ${gross_pay * 0.8:.2f}\n")

        


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
        tax_amount = self.calculate_tax_amount(tax_rate)

    def update_hours_worked(self, hours):
        self.hours_worked = hours

    def update_hourly_rate(self, rate):
        self.hourly_rate = rate

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Hours Worked: {self.hours_worked}, Hourly Rate: ${self.hourly_rate:.2f}, Gross Pay: ${self.calculate_gross_pay():.2f}, Net Pay: ${self.calculate_net_pay(0.2):.2f}, Tax Amount: ${self.calculate_tax_amount(0.2):.2f}"
    
    def sort_by_gross_pay(self, other):
        return self.calculate_gross_pay() - other.calculate_gross_pay()
    
    def sort_by_net_pay(self, other, tax_rate):
        return self.calculate_net_pay(tax_rate) - other.calculate_net_pay(tax_rate)
    
    def sort_by_employee_id(self, other):
        return self.employee_id - other.employee_id
    
    
    
