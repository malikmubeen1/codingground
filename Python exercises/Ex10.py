# Ex. 10

# demonstrate escape quotes
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Backslash \\"
print "single quote: \' "
print "double quote: \" "
print "ascii bell \a "
print "ascii bs back\bspace"
print "ascii formfeed \f formfeed"
print "ascii linefeed \n second line"
print "\r carriage \r return"
print "tab\ttab"
print "vertical\vtab"

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
        