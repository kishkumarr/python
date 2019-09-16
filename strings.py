
string = "hello this is Kishore."

capitalized_string = string.capitalize()

print('Old String-', string)
print('Capitalized String-', capitalized_string)


string = "* is an operator."

new_string = string.capitalize()

print('Old-', string)
print('New-', new_string)


string = "Python is cool, isn't it?"
substring = "is"

count = string.count(substring)

print("The count is=", count)


a1 =  {'2', '1', '3'}
s = ', '
print(s.join(a1))

a1 = {'car', 'bike', 'bus'}
s = '->->->->->->'
print(s.join(a1))




s = 'Python Is Bad.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '15 Is A Number'
print(s.istitle())

s = 'RUBY'
print(s.istitle())




text= 'Love non veg'

print(text.split())

grocery = 'Milk, Chicken, Bread'

print(grocery.split(', '))

print(grocery.split(':'))
