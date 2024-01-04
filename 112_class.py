# class


class Person:  # naming convention capitalize "P", also, it should be a "noun", e.g. Person, Fruit, Animal, Vehicle

  def __init__(self, name2: str, age: int):  # self instance of class
    self.name = name2  # name & age are "property"
    self.age = age

  def __str__(self):  # toString()
    return f"{self.name} is {self.age} years old."  # f-string

  def greet(self, to):  # greet() is a method (function in class)
    print(self.name + ' says hello to', to)


johnny = Person('John', 10)
print(johnny)

tom = Person('Thomas', 11)
print(tom)

tom.greet('Mary')  # Thomas says hello to Mary

######################################################
print('class inheritance')

class Student(Person):  # Student is a subclass of Person

  def __init__(self, name, age, grade):  # instantiate
    super().__init__(name, age)  # super() is to inherit from parent class
    self.grade = grade

  def __str__(self):
    return f"{self.name} is {self.age} years old and is in {self.grade} grade......"


mike = Student('Michael', 12, 'S.1')
print(mike)
mike.greet('Alex')

