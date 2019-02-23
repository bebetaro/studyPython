def triangle(bottom, height):
    return float(bottom * height/2)


bottom = input("Please input bottom line length: ")
height = input("Please input height: ")

print(triangle(int(bottom), int(height)))
