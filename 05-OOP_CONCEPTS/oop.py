# Class definition
class dog:
    # class attributes
    num_of_legs = 4

    #instance attribute
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color 
        self.breed = breed

# Class definition
class parrot:
    # class attributes
    num_of_legs = 2

    #instance attribute
    def __init__(self, name, color, beak_color):
        self.name = name
        self.color = color
        self.beak_color = beak_color

# Creating instances of a parrot class
tommy = dog('tommy', 'black', 'labrador')
rubolf = dog('rubolf', 'white', 'Geman Shephard')
print(f'Tommy has {tommy.num_of_legs} legs, it is {tommy.color} in color and its breed is {tommy.breed}')
print(f'Rubolf has {rubolf.num_of_legs} legs, it is {rubolf.color} in color and its breed is {rubolf.breed}')

# Creating instances of a parrot class
charlie = parrot('charlie', 'green', 'red')
print(f'Charlie has {charlie.num_of_legs} legs, it is {charlie.color} in color it has beak in {charlie.beak_color} in color')