class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

class Student:
    def __init__(self, name, grade, school):
        self.name = name
        self.grade = grade
        self.school = school


car1 = Car("Tesla Model S", "Black", 2022)
car2 = Car("Ford Mustang", "Red", 2020)
car3 = Car("Chevrolet Camaro", "Blue", 2021)

animal1 = Animal("Dog", "Max", 5)
animal2 = Animal("Cat", "Whiskers", 3)
animal3 = Animal("Rabbit", "Bunny", 2)

student1 = Student("John", 10, "Springfield High")
student2 = Student("Anna", 8, "Lakeview School")
student3 = Student("David", 12, "Oakwood Academy")

print(f"Car1: {car1.model}, {car1.color}, {car1.year}")
print(f"Animal1: {animal1.species}, {animal1.name}, {animal1.age}")
print(f"Student1: {student1.name}, Grade: {student1.grade}, School: {student1.school}")