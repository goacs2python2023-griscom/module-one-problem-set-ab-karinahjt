#Write a Python function that computes the cost of a road trip, given the distance traveled, 
# the fuel efficiency of the car (in miles per gallon), and the cost of a gallon of gas.
def rtCost(d,f,c):
    if f <= 0:
      return "error"
    return ((d/f)*c)

print (rtCost(714.0,47.0,3.7))
print (rtCost(714.0,0.0,3.7))