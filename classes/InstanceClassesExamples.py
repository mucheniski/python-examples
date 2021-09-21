#  Instance of Circle
from classes.Circle import Circle

redCircle = Circle(2, "Red")
greenCircle = Circle(3, "Green")

# Acces atributes
print(redCircle.color)

# Changing values
redCircle.color = "Blue"

# Changing size with method
redCircle.increase_size(4)

print(redCircle.draw_circle())

# details of the class
print(dir(Circle))