#coding:utf-8


if __name__ == '__main__':
    print('OK')
    # 呼び出し方1
    from lib1 import test1
    test1.test_func1()
    # 呼び出し方2
    import lib1.test1
    lib1.test1.test_func1()
    
    from lib2 import test_func2
    test2.test_func2()
