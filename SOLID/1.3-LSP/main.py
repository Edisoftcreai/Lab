class Employee:
    def __init__(self, base_salary: float):
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        raise NotImplementedError("Subclasses should implement this method.")

class FullTimeEmployee(Employee):
    def __init__(self, base_salary: float, bonus: float):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate: float, hours_worked: float):
        # Base salary is not used here, which creates an inconsistency
        super().__init__(0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked