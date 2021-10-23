# read animals.txt
file = open('animals.txt', 'r')
animals = file.readlines()
file.close()

# and write animals_new.txt
file = open('animals_new.txt', 'w')
for animal in animals:
    file.write(animal.replace('\n', ' '))
file.close()
