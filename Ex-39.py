"""
Exercise 39: Sound Levels

The following table lists the sound level in decibels for several common noises.

Noise	    Decibel level (dB)
Jackhammer	    130
Gas lawnmower	106
Alarm clock	    70
Quiet room	    40

Write a program that reads a sound level in decibels from the user.
If the user enters a decibel level that matches one of the noises in the table then your program should display a message containing only that noise.
If the user enters a number of decibels between the noises listed then your program should display a message indicating which noises the level is between.
Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, and for a value larger than the loudest noise in the table.
"""
if __name__ == '__main__':
    _input = int(raw_input("Enter the sound level in decibels:"))
    if _input == 40:
        print "Quiet room"
    elif _input>40 & _input<70:
        print "between Quiet room and Alarm clock"
    elif _input == 70:
        print "Alarm clock"
    elif _input>70 & _input<106:
        print "between Alarm clock and Gas lawnmower"
    elif _input == 106:
        print "Gas lawnmower"
    elif _input>106 & _input<130:
        print "between Alarm clock and Jackhammer"
    elif _input == 130:
        print "Jackhammer"
    elif _input <40 | _input >130:
        print "no sound in the table ><"