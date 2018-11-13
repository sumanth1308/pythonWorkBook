"""
Exercise 6:Tax and Tip

The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user.
Then your program will compute the tax and tip for the meal.
Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax).
The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip.
Format the output so that all of the values are displayed using two decimal places.
"""
if __name__ == '__main__':
    _cost = float(raw_input("Enter the cost of the meal order :"))
    _tax = _cost * 0.08     #8% tax
    _tip = _cost * 0.18
    print "Meal\t\t: $%.2f" % _cost
    print "Tax \t\t: $%.2f" % _tax
    print "Tip \t\t: $%.2f" % _tip
    print "Total\t\t: $%.2f" % (_cost+_tax+_tip)
    print "Grand Total : $%d" % round(_cost+_tax+_tip)
    
    