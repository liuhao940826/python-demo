# encoding:UTF-8
def test_while_yield():

    yield "哈哈哈"

    yield "下面的我"

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
    result = test_while_yield()
    print("结果:{}".format(next(result)))
    print("结果:{}".format(next(result)))





