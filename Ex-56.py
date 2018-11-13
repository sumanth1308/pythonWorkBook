"""
Exercise 56: Cell Phone Bill

A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month.
Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each.
All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is subject to 5 percent sales tax.
Write a program that reads the number of minutes and text messages used in a month from the user.
Display the base charge, additional minutes charge (if any), additional text message charge (if any), the 911 fee, tax and total bill amount.
Only display the additional minute and text message charges if the user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""
if __name__ == '__main__':
    try:
        print "Please enter the required details"
        _airTime = int(raw_input("Enter the Airtime used:"))
        _noOfMsg = int(raw_input("Enter the number of msg sent:"))
        print "\n"
        
        _costWithoutTax = 0
        _costWithoutTax += 15.00
        print "Base price of your plan \t:\t$15.00"
        
        if _airTime < 50:
            _extraAirTimeCost = 0
        else:
            _extraAirTimeCost = (_airTime - 50) * 0.25
        _costWithoutTax += _extraAirTimeCost
        print "Extra air time cost\t\t\t:\t$%.2f" % _extraAirTimeCost
        if _noOfMsg < 50:
            _extraMsgCost = 0
        else:
            _extraMsgCost = (_noOfMsg - 50) * 0.15
        _costWithoutTax += _extraMsgCost
        print "Extra Msg cost\t\t\t\t:\t$%.2f" % _extraMsgCost
        
        _costWithoutTax += 0.44
        print "Support 911 call centers \t:\t$0.44"
        
        _tax = _costWithoutTax * 0.05
        print "Tax\t\t\t\t\t\t\t:\t$%.2f" % _tax
        _totalCost = _costWithoutTax + _tax
        
        print "---------------------------------------"
        print "Total Bill amount\t\t\t:\t$%.2f" % _totalCost
        print "---------------------------------------"
    except:
        print "Something failed please check the code."
        