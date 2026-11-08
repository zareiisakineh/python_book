# file: ex_08_07_student_register_start.py

class Student:
    _student_count = 0

    def __init__(self, name, student_id, gpa):
    # TODO: Create the constructor with parameters name, student_id and gpa.
        self._name = name
        self._student_id = student_id
        self._gpa = gpa
     #       Store the student data and update the shared student count.    
        Student._student_count += 1
   

    @classmethod
    def get_count(cls):
    # TODO: Create the class method get_count().
    #       A class method uses cls instead of self.
    #       Remember the decorator that marks a method as a class method.
    #       Return the total number of Student objects created.
        return cls._student_count
    # TODO: Create a property named gpa.
    #       First create the getter. Remember that a property getter is an
    #       instance method and uses the @property decorator.
    @property
    def gpa(self):
        return self._gpa

    # The setter is provided because exceptions have not been covered yet.
    # Complete it by storing the valid GPA.
    @gpa.setter
    def gpa(self, value):
        if not 0.0 <= value <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # TODO: Store the valid GPA.
        self._gpa = value 
            
    # TODO: Create __str__() as an instance method.
    #       Return a readable string containing name, ID and GPA.
    def __str__(self):
        return f"{self._name}, {self._student_id}, {self._gpa}"
    # TODO: Create __lt__() as an instance method.
    #       It receives another Student object in addition to self.
    #       Compare the students by GPA.
    def __lt__(self, other):
        return self._gpa < other._gpa

class StudentRegister:

    # def __init__(self):
    # TODO: Create the constructor.
    #       Each register should start with its own empty list of Student objects.
    def __init__(self):
        self._students = []
        
    # TODO: Create the instance method add().
    #       It needs self and the Student object to add.
    def add(self, student):
        self._students.append(student)
       
        
    # TODO: Create the instance method remove_by_id().
    #       It needs self and the student ID to remove.
    #       If the ID is not found, leave the register unchanged and print
    #       a clear message.
    def remove_by_id(self, student_id):
        for student in self._students:
            if student.student_id == student_id:
                self._Students.remove(student)
                return
            
        print(f"{student_id} finnes ikke")
            

    # TODO: Create the instance method find_by_name().
    #       It needs self and the name to search for.
    #       Return all case-insensitive partial name matches as a list.
    def find_by_name(self, name):
        matches = []
        for student in self._students:
            if name.lower() in student._name.lower():
                matches.append(student)
        return matches
        
    # TODO: Create the instance method top_students().
    #       It needs self and n.
    #       Return up to n students in descending GPA order.
    #       Use the Student comparison.
    def top_students(self, n):
        return sorted(self._students, reverse=True)[:n]
        
        
    # TODO: Create __len__() as an instance method.
    #       Return the number of students in this register.
    def __len__(self):
        return len(self._students)
        

    # TODO: Create __str__() as an instance method.
    #       Return all students, one per line.
    def __str__(self):
        resultat = ""
        
        for student in self._students:
            resultat += f"{student} \n"
        
        return resultat
            

# CLIENT CODE
#
# The code below demonstrates how the classes should be used.
# Uncomment it when you have implemented the classes and methods above.
# You can then run the file to test your implementation.

reg = StudentRegister()
reg.add(Student("Alice Johnson", 1001, 3.9))
reg.add(Student("Bob Olsen", 1002, 2.8))
reg.add(Student("Clara Lee", 1003, 3.7))
reg.add(Student("David Park", 1004, 3.2))
#
print(f"Register has {len(reg)} students.\n")
#
print("Top 2 students:")
for s in reg.top_students(2):
     print(f"  {s}")
#
print("\nSearch for 'o':")
for s in reg.find_by_name("o"):
    print(f"  {s}")
#
print(f"\nTotal students created: {Student.get_count()}")