class Employee:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.department = ""
        self.hourlySalary = 15.0

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name

class Blah:
    def __int__(self, dur:float="dur"):
        self.dur=dur

        if not isinstance(dur, float):
            raise Exception("Invalid Param")

def greet(name:str)->str:
    greeting = 'Hello, ' + name
    return greeting

if __name__ == "__main__":
    e1 = Employee()
    e1.setName("George")
    Employee.setName(e1, "James")
    e1.name = "Gorge"

    e1.fav_color = "red"
    del e1.name
