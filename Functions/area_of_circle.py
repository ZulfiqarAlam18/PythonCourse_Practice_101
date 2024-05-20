import math

def area_of_circle(radiu):
    area = math.pi*(radius**2)
    return area

radius = int(input("Enter raduis of Circle :"))

print(f"The area of cirlce having radius {radius} is {area_of_circle(radius)}")