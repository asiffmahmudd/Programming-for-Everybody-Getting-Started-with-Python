hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))

if hrs <= 40 :
    print(hrs*rate)
else:
    x = rate*40+rate*1.5*(hrs-40)
    print(x)