class Employee: 
    """A class to represent an employee"""
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    """A class to represent an employee"""
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary    

    def calculate_paycheck(self):
        """Calculate the weekly paycheck"""
        return self.salary / 52
   
class HourlyEmployee(Employee):
    """A class to represent an employee"""
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)    
        self.hourly_rate = hourly_rate
        self.weekly_hours = weekly_hours

    def calculate_paycheck(self):
        """Calculate the weekly paycheck"""
        return self.hourly_rate * self.weekly_hours
    
class CommissionEmployee(SalaryEmployee):
    """A class to represent an employee"""
    def __init__(self, fname, lname, salary, sales_num, commission_rate):
        super().__init__(fname, lname, salary)
        self.commission_rate = commission_rate
        self.sales_num = sales_num

    def calculate_paycheck(self):
        """Calculate the weekly paycheck"""
        return self.salary / 52 + self.sales_num * self.commission_rate    