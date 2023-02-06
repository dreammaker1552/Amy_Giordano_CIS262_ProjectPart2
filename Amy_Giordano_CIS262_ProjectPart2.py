def get_dates():
      from_date = input("Enter from date (mm/dd/yyyy): ")
      to_date = input("Enter to date (mm/dd/yyyy): ")
      return from_date, to_date

from_date = []
to_date = []
employee_name = []
total_hours = []
hourly_rate = []
income_tax = []

employee_info = [from_date, to_date, employee_name, total_hours, hourly_rate, income_tax]

def get_employee_name():
      employee_name = input("Enter employee name: ")
      return employee_name
 
def get_total_hours():
    return float(input("Enter total hours worked: "))
 
def get_hourly_rate():
      hourly_rate = float(input("Enter hourly rate: "))
      return hourly_rate

def get_income_tax_rate():
      income_tax = float(input("Enter income tax: "))
      return income_tax

def calculate_pay(total_hours, hourly_rate, income_tax):
      gross_pay = total_hours * hourly_rate
      income_tax = gross_pay * income_tax
      net_pay = gross_pay - income_tax
      return gross_pay, income_tax, net_pay

def display_employee_data(from_date, to_date, employee_name, total_hours, hourly_rate, income_tax, gross_pay, net_pay):
      print("From date:", from_date)
      print("To date:", to_date)
      print("Employee name:", employee_name)
      print("Total hours worked:", total_hours)
      print("Hourly rate:", hourly_rate)
      print("Income tax:", income_tax)
      print("Gross pay:", gross_pay)
      print("Net pay:", net_pay)

def display_total_data(total_data):
    print("Total number of employees:", total_data[total_employees])
    print("Total hours worked:", total_data[total_hours])
   
employee_data = []
total_data = {"total_employees": 0, "total_hours": 0,}

while True:
    name = input("Enter employee name (enter 'q' to quit): ")
    if name == 'q':
        break
    
    from_date, to_date = get_date_range()
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    income_tax = float(input("Enter income tax rate: "))
        
    employee_data.append({
        "from_date": from_date,
        "to_date": to_date,
        "name": name,
        "hours": hours,
        "rate": rate,
        "tax_rate": tax_rate,
        "tax": tax,
        "net_pay": net_pay
    })

    totals["total_employees"] += 1
    totals["total_hours"] += hours
    totals["total_tax"] += tax
    totals["total_net_pay"] += net_pay

for employee in employee_data:
    display_employee_data(employee["from_date"], employee["to_date"], employee["name"],
                         employee["hours"], employee["rate"], employee["tax"], employee["net_pay"])

display_totals(totals["total_employees"], totals["total_hours"], totals["total_tax"],      totals["total_net_pay"])



while True:
	name = get_employee_name()
	if name == "End":hours = get_total_hours()
rate = get_hourly_rate()
tax_rate = get_tax_rate()
gross_pay, tax, net_pay = calculate_pay(hours, rate, tax_rate)
display_employee_pay(name, hours, rate, gross_pay, tax_rate, tax, net_pay)
num_employees += 1
total_hours += hours
total_gross_pay += gross_pay
total_tax += tax
total_net_pay += net_pay
 
display_summary(num_employees, total_hours, total_gross_pay, total_tax, total_net_pay)


