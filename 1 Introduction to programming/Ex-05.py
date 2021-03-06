"""
Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.
In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be received for returning those containers.
Format the output so that it includes a dollar sign and always displays exactly two decimal places.
"""
if __name__ == '__main__':
    _1LiterContainer = int(raw_input("Number of 1 Liter Containers:"))
    _moreThan1LiterContainer = int(raw_input("Number of more than 1 Liter Containers:"))
    _refund = _1LiterContainer * 0.10 + _moreThan1LiterContainer * 0.25
    print "You will get a refund of $%.2f" % _refund