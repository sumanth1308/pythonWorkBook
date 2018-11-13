"""
Exercise 4:Area of a Field
Create a program that reads the length and width of a farmer's field from the user in feet.
Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""
if __name__ == '__main__':
    _width = float(raw_input("Enter width:"))
    _length = float(raw_input("Enter length:"))
    _area = _width*_length
    _areaInAcre = _area/43560
    print "Area of the room :%f acre" % _areaInAcre