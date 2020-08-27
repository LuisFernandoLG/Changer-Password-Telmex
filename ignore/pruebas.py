class persona():
    def __init__(self, name):
        self.name = name

    def sayName(self, name = None):
        if name == None:
            return "My name is " + self.name
        else:
            return f"My new name is {name}"



luis = persona("Luis")

print(luis.sayName())