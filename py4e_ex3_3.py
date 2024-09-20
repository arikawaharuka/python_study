score = input("Enter Score: ")
try:
    sre = float(score)
except:
    print("Error,please enter numeric input")
    quit()
if sre < 0 or sre > 1:
    print("please enter the value within the range,poor guy!")
    quit()
else:
    if sre >= 0.9:
        print("A")
    elif sre >= 0.8:
        print("B")
    elif sre >= 0.7:
        print("C")
    elif sre >= 0.6:
        print("D")
    else:
        print("F")
