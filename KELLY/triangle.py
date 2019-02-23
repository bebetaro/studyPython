def triangle(bottom, height):
    return bottom * height/2


bottom = input("Please input bottom line length: ")
height = input("Please input height: ")

print(triangle(float(bottom), float(height)))
