# Scenario:


You are developing a salary calculation system for a company where different types of employees need to have their salaries calculated. The base class Employee provides a common interface for salary calculation, and you have subclasses for FullTimeEmployee and PartTimeEmployee. The challenge is to ensure that these subclasses adhere to the Liskov Substitution Principle (LSP) so they can be used interchangeably wherever an Employee is expected.