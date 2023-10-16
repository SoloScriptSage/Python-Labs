class Employee: #creating-kind-of-abstract-class
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

    def calcPay(self):
        return 0

    def __str__(self):
        return f"Name: {self.__name}\nID: {self.__employee_id}\n"

class HourlyEmployee(Employee): #inherited-classes
    def __init__(self, name, employee_id, hours_worked, hourly_pay_rate):
        super().__init__(name, employee_id)
        self.__hours_worked = hours_worked
        self.__hourly_pay_rate = hourly_pay_rate

    def calcPay(self): #override-for-hourly
        return self.__hours_worked * self.__hourly_pay_rate

    def __str__(self):
        return super().__str__() + f"Hours Worked: {self.__hours_worked}\nHourly Pay Rate: ${self.__hourly_pay_rate:.2f}\nGross Pay: ${self.calcPay():.2f}"

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary, num_pay_periods):
        super().__init__(name, employee_id)
        self.__annual_salary = annual_salary
        self.__num_pay_periods = num_pay_periods

    def calcPay(self): #override-for-salaried
        return self.__annual_salary / self.__num_pay_periods

    def __str__(self):
        return super().__str__() + f"Annual Salary: ${self.__annual_salary:.2f}\nNum Pay Periods: {self.__num_pay_periods}\nGross Pay: ${self.calcPay():.2f}"

def main():
    #creating-a-list-for-employers
    employees = [
        HourlyEmployee("Vladyslav Hirchuk", 25033, 40, 55.0),
        SalariedEmployee("Henson Michael", 1023, 15000000, 26), #my-professor-is-multimillioner
    ]

    #show-up
    for employee in employees:
        print(employee)
        print()

    #wow!!-method-for-summarizing
    total_payroll = sum(employee.calcPay() for employee in employees)

    print(f"Total Payroll: ${total_payroll:.2f}")

if __name__ == "__main__":
    main()

