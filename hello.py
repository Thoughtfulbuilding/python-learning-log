print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
if my_name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger')
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
if my_age < 12:
    print('You are not Alice, kiddo.')
elif my_age > 12:
    print('You will be ' + str(int(my_age) + 1) + ' in a year.')# Write your code here :-)
