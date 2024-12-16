def computepay(h, r):
    if h <= 40:
        return h*r
    else:
        return (h-40)*r*1.5+40*r

hrs = input("Enter Hours:")
rph = input("Enter Rate per hours:")
whs = float(hrs)
rate = float(rph)
p = computepay(whs, rate)
print("Pay", p)