#coding:utf-8


if __name__ == '__main__':
    print('OK')
    # $B8F$S=P$7J}(B1
    from lib1 import test1
    test1.test_func1()
    # $B8F$S=P$7J}(B2
    import lib1.test1
    lib1.test1.test_func1()
    
    from lib2 import test_func2
    test2.test_func2()
