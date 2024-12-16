hrs = input("Enter Hours:")
rph = input("Enter Rate per hours:")
try:
    h = float(hrs)
    rate = float(rph)
except:
    print("Error,please enter numeric input")
    quit()
    
if h <= 40:
    gpay = h*rate
else:
    gpay = (h-40)*rate*1.5+40*rate
print(gpay)