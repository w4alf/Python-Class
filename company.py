from employee import Employee

class Company:
    """A company class that holds a list of employees"""
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

def main():
    """Main function"""
    my_company = Company()
    my_company.add_employee(Employee("John", "Doe", 50000))
    my_company.add_employee(Employee("Jane", "Smith", 60000))
    my_company.add_employee(Employee("Joe", "Brown", 70000))

   # print(my_company.employees)
   
    for employee in my_company.employees:
        #the f'' is a formatted string using commas and 2 decimal places
        print(f"{employee.fname} {employee.lname} makes ${employee.calculate_paycheck():,.2f} per week.")
        print("-------------------------------------")

main()


    