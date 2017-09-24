animals = ['Dog ','Cat ','Lion ','Tiger ','Giraffe ','Elephant']
for i in animals:
    print(i)
print('A '+ animals[0] + 'Would be a great companion')
print(animals[1] + 'Can be a cute pet')
print(animals[2] + 'is a very big animal')

for i in animals:
    print(i + 'walks on four legs')

print('the first three items in the list are:')
for i in animals[:3]:
    print(i)

print('three items from the middle of the list are: ')
animals.append('big')
animals.append('small')
for i in animals[1:4]:
    print(i)

print('the last three items in the list are: ')
for i in animals[2:5]:
    print(i)
