from Employee import Employee

working_hour_0 = 0
working_hour_1 = 0

name_0 = input("Name of the 0.Emloyee => ")
hourly_rate_0 = int(input("hourly_rate of the 0.Emloyee => "))
#print(Employee.hourly_rates)
name_1 = input("Name of the 1.Emloyee => ")
hourly_rate_1 = int(input("hourly_rate of the 1.Emloyee => "))
emloye_0 = Employee(name_0, hourly_rate_0, working_hour_0)
emloye_1 = Employee(name_1, hourly_rate_1, working_hour_1)
print(emloye_0.__str__())
print(emloye_1.__str__())
working_hour_0 = (int(input("working_hours of 0.Employee => "))) 
working_hour_1 = (int(input("working_hours of 1.Employee => ")))
setattr(emloye_0, "working_hour", working_hour_0)
setattr(emloye_1, "working_hour", working_hour_1)
#print(emloye_0.working_hour)
#print(emloye_1.working_hour)
salary_0 = (emloye_0.salary())
salary_1 = (emloye_1.salary())
print("Salary of employee0 = ", salary_0)
print("Salary of employee1 = ", salary_1)
print(Employee.__eq__(salary_1, salary_0))





