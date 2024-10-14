class Employee:
    
    hourly_rates = 0
    def __init__(self, name, hourly_rate, working_hour):
        self.name = name
        self.hourly_rates = hourly_rate
        self.working_hour = working_hour
    
    def __str__(self):
        return "Employee(" + str(self.name) + ") wors with hourly_rate = " + str(self.hourly_rates)
        
    def salary(self):
        return self.hourly_rates * self.working_hour
    
    def __eq__(salary_0, salary_1):
        if salary_1 == salary_0:
            return "Do they have the same salary = " + str(True)
        else:
            return "Do they have the same salary = " + str(False)
    
    