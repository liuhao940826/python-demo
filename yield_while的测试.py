# encoding:UTF-8
def test_while_yield():
    print("我进来了")
    page = 0
    # while True:
    #     print("我也进来了")
    #     page += 1
    #     if page > 3:
    #         print("我现在是:", page)
    #         yield page
    #     print("我被调用了")

if __name__ == '__main__':
    print("我被执行了")
    test_while_yield()
    print("我被输出了.....")





