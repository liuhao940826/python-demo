import datetime

# 范围时间
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '15:00', '%Y-%m-%d%H:%M')

print("d_time;{}".format(d_time))
print("d_time1;{}".format(d_time1))


# 当前时间
n_time = datetime.datetime.now()
print("n_time;{}".format(n_time))

# 判断当前时间是否在范围时间内
if n_time > d_time and n_time < d_time1:
    print("这是真的")
