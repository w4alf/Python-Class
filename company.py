from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    """A company class that holds a list of employees"""
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    def display_employees(self):
        for employee in self.employees:
            print(employee.fname,employee.lname)
            print("-------------------------------------")  

    def pay_employees(self):
        for employee in self.employees:
            print(f"{employee.fname} {employee.lname} makes ${employee.calculate_paycheck():,.2f} per week.")
            print("-------------------------------------") 

    def calculate_payroll(self):
        """Calculate the total payroll for the week"""
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_paycheck()
        return total_payroll            

def main():
    """Main function"""
    my_company = Company()
    my_company.add_employee(SalaryEmployee("John", "Doe", 50000))
    my_company.add_employee(HourlyEmployee("Jane", "Smith", 40, 24))
    my_company.add_employee(CommissionEmployee("Joe", "Brown", 60000, 15000, 0.1))

    my_company.display_employees()
    my_company.pay_employees()
    my_company.calculate_payroll()
    print(f"The total payroll for the week is ${my_company.calculate_payroll():,.2f}")


    #for employee in my_company.employees:
    #    #the f'' is a formatted string using commas and 2 decimal places
    #    print(f"{employee.fname} {employee.lname} makes ${employee.calculate_paycheck():,.2f} per week.")
    #    print("-------------------------------------")

main()


    