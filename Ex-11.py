"""
Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed in miles-per gallon(MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km).
Use your research skills to determine how to convert from MPG to L/100 km.
Then create a program that reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian units.
"""
if __name__ == '__main__':
    _MPG = int(raw_input("Enter fuel efficiency:"))
    #100 KMPL = 235.214583 MPG => KMPL = 2.35214583 MPG
    KMPL = 2.35214583 * _MPG
    print "fuel efficiency in canadian units: ",KMPL," liters-per-hundred kilometers"
    