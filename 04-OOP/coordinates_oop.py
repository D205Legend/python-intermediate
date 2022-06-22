# Creating a Class called Coordinates
# This provides a template or a blueprint for a point on a plane
class Coordinate:
    x = None
    y = None

    def display(self):
        print(f'X = {self.x}, Y = {self.y}')


# c1 is a point (5, 7) which is an instance of a Coordinate class
c1 = Coordinate()
c1.x = 5
c1.y = 7

c1.display()
