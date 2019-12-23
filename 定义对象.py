import json
import time

import numpy as np


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, time):
            return obj.__str__()
        else:
            return super(NpEncoder, self).default(obj)

class MySqlConfig:
    host='localhost'
    port=3306
    user='root'
    password='123456'
    charset='utf8mb4'


class Config:
    user_id_list:[]
    filter = 1
    since_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    write_mode= ["csv"]
    original_pic_download= 1
    retweet_pic_download=0
    original_video_download=1
    retweet_video_download= 0
    mysql_config = MySqlConfig()


config =Config()
print(json.dumps(config))

