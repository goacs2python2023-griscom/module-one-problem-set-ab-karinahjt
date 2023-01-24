#Write a function that takes two arguments, one is the bill and the other is the percentage tip you would like to leave.
#  The function should return the total for the bill.
def tipCalc (a,b):
    return a+(a*b/100)

print (tipCalc(54,25))