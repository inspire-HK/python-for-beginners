# https://www.w3schools.com/python/python_dictionaries.asp

john = {'name': 'John', 'age': 10, 'gender': 'male'}  # aka object in other languages
sam = {'age': 11, 'gender': 'not sure', 'name': 'Sam'}
# age is a property, 11 is property value
print(john, type(john), len(john))
print(sam, type(sam), len(sam))

# print('##########################')

# print('John is', john['age'], 'year old')

sam['name'] = 'Samantha'  # update sam's name
sam['gender'] = 'female'
print('updated sam', sam)

# instantiate a new dict
peter = dict(name='Peter', age=12, gender='male')
print('Peter is', peter, type(peter))
