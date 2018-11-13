"""
Exercise 3:Area of a Room
Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the area of the room.
The length and the width will be entered as foating point numbers.
Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.
"""
if __name__ == '__main__':
    _width = float(raw_input("Enter width:"))
    _length = float(raw_input("Enter length:"))
    _area = _width*_length
    print "Area of the room :%f sqr feet" % _area