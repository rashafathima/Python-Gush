# parent class
class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def eDetail(self):
        print("---THIS IS PARENT CLASS---")
        print("Position: %s" %self.id)
        print("Name: %s" %self.name)

# child class (extension)
class Manager(Employee):

    def __init__(self, id, name, project):
        super().__init__(id, name)
        self.project = project

    def pDetail(self):
        print(" ")
        print("---THIS IS CHILD CLASS---")
        print("Project: %s" %self.project)


# creating objects
obj = Manager('Data Analyst', 'Rasha', 'Stock Prediction')

obj.eDetail()

obj.pDetail()
