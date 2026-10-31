# file: ex_08_02_employee_start.py

class Employee:
    _employee_count = 0  # class variable

    def __init__(self, name, employee_id, department, salary):
        # TODO: store all attributes with leading underscore
        self._name = name
        self._employee_id = employee_id
        self._department = department
        self._salary = salary
        
        # TODO: increment _employee_count
        Employee._employee_count += 1

    def give_raise(self, amount):
        # TODO: increase salary by amount
        if amount <= 0:
            print(f"{amount} kan ikke være negativ")
        else:   
            self._salary += amount
        # Reject negative or zero amounts with a message
        

    def annual_salary(self):
        # TODO: return monthly salary * 12
        return self._salary * 12

    @classmethod
    def get_employee_count(cls):
        # TODO: return total number of employees created
        return cls._employee_count

    def __str__(self):
        # TODO: return formatted string with all attributes
        return f"navn: {self._name}\n ansatt-nummer: {self._employee_id}\n avdeling: {self._department}\n  lønn: {self._salary}"

    def __eq__(self, other):
        # TODO: equal if same employee_id
        return self._employee_id == other._employee_id
    
# lt betyr less than
    def __lt__(self, other):
        # TODO: compare by salary
        return self._salary < other._salary
    
# gt betyr greater than
    def __gt__(self, other):
        # TODO: compare by salary
        return self._salary > other._salary


if __name__ == "__main__":
    e1 = Employee("Alice Johnson", 1001, "Engineering", 65000)
    e2 = Employee("Bob Smith",     1002, "Marketing",   55000)
    e3 = Employee("Clara Lee",     1003, "Engineering", 72000)

    print(e1)
    print(f"Annual salary: {e1.annual_salary()}")
    e1.give_raise(5000)
    print(f"After raise:   {e1.annual_salary()}")
    e1.give_raise(-1000)

    print(f"\nEmployees created: {Employee.get_employee_count()}")
    print(f"\ne1 == e2? {e1 == e2}")
    best = max(e1, e2, e3)
    print(f"Highest salary: {best._name} ({best._salary}/month)")
