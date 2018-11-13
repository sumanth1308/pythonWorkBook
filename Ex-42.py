"""
Exercise 42: Frequency To Note

In the previous question you converted from note name to frequency.
In this question you will write a program that reverses that process.
Begin by reading a frequency from the user.
the frequency is within one Hertz of a value listed in the table in the previous question then report the name of the note.
Otherwise report that the frequency does not correspond to a known note. In this exercise you only need to consider the notes listed in the table.
There is no need to consider notes from other octaves.

"""

if __name__ == '__main__':
    _freq = float(raw_input("Enter the frequency:"))
    if _freq <= 261.63 + 1 and _freq >= 261.63 - 1:
        print "C4"
    elif _freq <= 293.66 + 1 and _freq >= 293.66 - 1:
        print "D4"
    elif _freq <= 329.63 + 1 and _freq >= 329.63 - 1:
        print "E4"
    elif _freq <= 349.23 + 1 and _freq >= 349.23 - 1:
        print "F4"
    elif _freq <= 392.00 + 1 and _freq >= 392.00 - 1:
        print "G4"
    elif _freq <= 440.00 + 1 and _freq >= 440.00 - 1:
        print "A4"
    elif _freq <= 493.88 + 1 and _freq >= 493.88 - 1:
        print "B4"
    else:
        print "No note associated with your frequency"