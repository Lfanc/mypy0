def out(fun):
    def inner():
        fun1 = fun
        print("加了装饰器效果")
        fun1()
    return inner

def fun1():
    print("普通效果")

class tank:
    
    def __init__(self, a):
        self.a = a
    

fun2 = out(fun1)
fun2()