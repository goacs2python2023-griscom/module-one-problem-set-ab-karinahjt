#Write a function that determines the number of 52-passenger school buses needed to transport a given number of students

def bus(s):
    if (type(s) != int) or (s<=0):
        print("Error: provide the number of students as integer > 0")
        return
    if s % 52 != 0:
        print((int(s/52))+1)
    else:
        print(int(s/52))
    return

bus(-20)
bus(52)
bus(548)
