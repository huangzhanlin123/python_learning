###################### 3.3 递归 #############################

#3.3.1 递归的概念
'''
递归的本质就是在函数体中又调用函数本身
'''


#3.3.2 递归案例

'''
1、非递归案例
def get_factorial(num):

    res = 1
    for n in range(1,num+1):
        res *= n
    return res

print(get_factorial(5))

2、递归案例
def get_factorial2(n):

    return n*get_factorial2(n-1)if n>1 else 1

print(get_factorial2(5))

def get_factorial2(n):

    if n>1:
        return n * get_factorial2(n-1)
    else:
        return 1

print(get_factorial2(5))


'''


