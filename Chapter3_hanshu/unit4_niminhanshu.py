###################### 3.3 匿名函数 #############################


'''
1、普通传惨
def operater(a,b):

    return a+b

def function(a,b,operater):

    return operater(a,b)

print(function(1,2,operater))

2、匿名函数传参
def fun2(a,b,operater):

    return operater(a,b)

print(fun2(1,2,lambda x,y:x+y))


def functions(a,b):
    return a+b

def funss(a,b,functions):
    return functions(a,b)

print(funss(2,2,functions))


def funs(a,b,opaaa):
    return opaaa(a,b)

print(funs(5,2,lambda x,y:x+y))

'''






