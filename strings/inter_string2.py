name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Deanna'

greeting1 = "Product Purchase: {2} - hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

greeting2 = f"Product Purchase: {product} - hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting2)