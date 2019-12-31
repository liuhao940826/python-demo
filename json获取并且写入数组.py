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

    loadNewConfigDbNameAndTbName(config, dbnames)

    with open("config.json", "w") as dump_f:
        json.dump(config, dump_f, ensure_ascii=False)
