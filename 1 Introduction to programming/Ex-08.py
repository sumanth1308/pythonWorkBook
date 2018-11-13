"""
Exercise 8:Widgets and Gizmos

An online retailer sells two products: widgets and gizmos.
Each widget weighs 75 grams.
Each gizmo weighs 112 grams.
Write a program that reads the number of widgets and the number of gizmos in an order from the user.
Then your program should compute and display the total weight of the order.
"""
if __name__ == '__main__':
    _widgets = int(raw_input("Enter number of Widgets:"))
    _gizmos = int(raw_input("Enter number of Gizmos:"))
    _weight = _widgets * 75 + _gizmos *112
    print "Total weight is ", _weight," grams"