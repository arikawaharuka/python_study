hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate per hours:")
rate = float(rph)
if h <= 40:
    gpay = h*rate
else:
    gpay = (h-40)*rate*1.5+40*rate
print(gpay)