a = 10
d = 0
# if 如果  else 其他的所有情况  elif 如果另外一种情况，
# >,  <,  >=, <=, != 不等于, or 或者  and 同时
if d == None:
    print("it is False")
elif d==True:
    print("it is true")
# block has indent 每个程序区要有固定的空格
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
    else:
        print("nothing")    
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