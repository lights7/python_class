# range 范围，排列，排序
a=list(range(0,5))
print(a)
b=list(range(0,100,10))
print(b)
# define a function 子程序 
# def: define 定义 
# function 函数，子程序
# parameters: input or 输入
# output: result 结果
#  name  parameters (input) body
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