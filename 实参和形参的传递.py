def test2(*args):
    print('arg的内容:', args)


def test1(**dict_param):
    print('dict的内容:', dict_param)


test1(name='刘浩', age='26')

test2("1", "2", "3")


custom_settings = {
        'ITEM_PIPELINES': {
            'xingji.pipelines.Xj_anchor_dataPipeline': 100,
        }
    }

print("类型:", type(custom_settings))
