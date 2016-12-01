# BMI program

print "What is your weight, in pounds?",
weight = 0.453592*int(raw_input())
print "What is your height, in inches?",
height = 0.0254 * int(raw_input())

BMI = weight / (height*height)

print "Your BMI is %r" % BMI

if BMI >= 30:
    print "Wow, you are obese. lose some weight plz."

elif BMI >= 25:
    print "You are overweight"
