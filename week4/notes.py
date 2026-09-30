class Student(Person):
    def __init__(self, id="123456", phone="999-999-999", address="123 Fake Stree", name="None"):
        self.id = id
        super().__init(phone, address, name)

class Person():
    def __init__(self, phone, address, name):
        self.phone = phone
        self.adress = address
        self.name = name