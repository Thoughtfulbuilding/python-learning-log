my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I don not have a pet named ' + name)
else:
    print(name + ' is my pet.')
    # Write your code here :-)
