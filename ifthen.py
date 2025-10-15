a = 10
d = 0
if d == None:
    print("it is False")
elif d==True:
    print("it is true")

if a==10:
    print("a=",a)
    print("a is greater than 8")
    b=int("10")
    b=float("10")
    print("a+b=",b)
    if a < 12 or a >16:
        string = str(a)
        string = string + " is a string now"
        print("a is less than 12",string)
        print("yes")
elif a<= 8 and  a > 0:
    print("a=",a)
    b=a
    print("b=",b)
elif a <-4:
    print("else if works")
elif a != -1:
    print("Can we get to here?")
else:
    print("a is out of range")