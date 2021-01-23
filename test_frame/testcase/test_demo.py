##fun和run自己随便定义叫啥都行
def b(fun):
    ###   *arge,**kwargs可以接受任意类型参数python语法
    def run(*arge,**kwargs):
        print("before 3333")
        #####这个是装饰的谁，谁就是这个fun
        fun(*arge,**kwargs)
        print("before 2222")
    return run

@b
def a():
    print('a')

def test_demo():
    a()
