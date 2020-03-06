import json

config = None


def loadNewConfigDbNameAndTbName(config, dbnames):
    tbnames = config['DEFAULT_TIEBA']
    tbnames.append('我新来的2')
    dbnames.setdefault('我新来的2', '新的db名字2')


with open('config.json', 'r', encoding='utf8') as f:
    config = json.loads(f.read())

    tbnames = config['DEFAULT_TIEBA']
    dbnames = config['MYSQL_DBNAME']
    shuzi = config.get("shuzi")
    fullCollectFlag= config.get("fullCollectFlag")

    print("数字的类型:{}".format(type(shuzi)))
    print("数字:{}".format(shuzi))

    print("标识的类型:{}".format(type(fullCollectFlag)))
    print("标识:{}".format(fullCollectFlag))

    loadNewConfigDbNameAndTbName(config, dbnames)

    with open("config.json", "w") as dump_f:
        json.dump(config, dump_f, ensure_ascii=False)
