#You are an olympic athlete who has just finished a race against three opponents.  
# Write a function that takes all four race times as arguments (your time as the first argument), 
# and returns a string describing the medal you just won ("gold", "silver", "bronze", or "no medal")
def my_medal (myt, t2, t3, t4):
    if (myt > t2):
        if (myt > t3):
            if (myt > t4):
                return "gold"
            elif (myt < t4):
                return "silver"
        elif (myt < t3): # < t3
            if (myt > t4):
                return "silver"
            elif (myt < t4):
                return "bronze"
    elif (myt < t2): # <=t2
        if (myt > t3):
            if (myt > t4):
                return "silver"
            elif (myt < t4):
                return "bronze"
        elif (myt < t3): # < t3
            if (myt > t4):
                return "bronze"
            elif (myt < t4):
                return "no medal"      
    return "error no ties"

print("My medal: ", my_medal(10.0, 10.1, 10.2, 10.3))  # no medal
print("My medal: ", my_medal(10.3, 10.2, 10.4, 10.6))  # bronze
print("My medal: ", my_medal(10.5, 10.2, 10.4, 10.6))  # silver
print("My medal: ", my_medal(10.8, 10.2, 10.4, 10.6))  # gold
print("My medal: ", my_medal(10.3, 10.3, 10.4, 10.6))   # error no ties
