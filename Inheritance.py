class Employee:

    def __init__(self, name):
        self.name = name

    def edetails(self):
        print("this is Employee section")


class Department:

    def __init__(self, depart, salary):
        self.depart = depart
        self.salary = salary

    def details(self):
        print("This is department section")


class Admin(Employee, Department):

    def __init__(self, name, depart, salary, id):
        self.name = name
        self.salary = salary
        self.depart = depart
        self.id = id

        Employee.__init__(self,name)
        Department.__init__(self,depart,salary)

    def control(self):
        print(f'Name of employee is {self.name} and his department is {self.depart} having salary of {self.salary} and his id number is {self.id}')


a = Employee("purushottam kumar")
b = Department("development",101010)
c = Admin("Purushottam kumar","Development",101010,5801)

a.edetails()
b.details()
c.control()
