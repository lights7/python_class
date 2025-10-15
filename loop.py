a=list(range(0,5))
print(a)
b=list(range(0,100,10))
print(b)
# define a function 子程序 
#  name  parameters body
def testfunc(name1):
    print ('hello %s' %name1)

testfunc('Alex')
testfunc('Ethan')
testfunc(a)
testfunc(10)

def testfunc2(name1,name2):
    print ('hello %s %s' % (name1,name2))

testfunc2('Felix','Lucas')
testfunc2(3.14,2.7)
testfunc('Zoeyyy')

def no_parm():
    aa=10
    bb=20
    return aa*bb

result=no_parm()
testfunc2(a,b)
#print(result)