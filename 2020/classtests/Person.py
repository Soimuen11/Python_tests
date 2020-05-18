class Person:

    def __init__(self, name, last_name, age, size, personality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.size = size
        self.personality = personality
    def describe_person(self, name, last_name, age, size, personality):
        print("Hello I am ", name, " ", last_name, " ", "and I am ", age, " years old.")
        print("I am ", size, " tall and I also am rather ", personality, ".")


individual1 = Person("Joey", "Biden", 50, "5ft10", "intelligent")
individual1.describe_person("Joey", "Biden", 50, "5ft10", "intelligent")
