def computepay(h,r):
    if h > 40:
        return 40*r+r*1.5*(h-40)
    else:
        return h*r

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)