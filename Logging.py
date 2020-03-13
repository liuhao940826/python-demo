import os
import logging
import logging.handlers



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取上级目录的绝对路径
log_dir = BASE_DIR + '/log/record.log'

# logging.basicConfig(level=logging.DEBUG,
#                     filename='output.log',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    # FileHandler
    file_handler = logging.FileHandler('record.log')
    file_handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # fh = logging.FileHandler(filename=log_dir,mode='a' ,encoding='utf-8',delay=0) #创建一个文件流并设置编码utf8
    # logger = logging.getLogger() #获得一个logger对象，默认是root
    # logger.setLevel(logging.DEBUG)  #设置最低等级debug
    # fm = logging.Formatter("%(asctime)s --- %(message)s")  #设置日志格式
    # logger.addHandler(fh) #把文件流添加进来，流向写入到文件
    # fh.setFormatter(fm) #把文件流添加写入格式
    return logger

if __name__ == '__main__':
    # logger.info('This is a log info')
    # logger.debug('Debugging')
    # logger.warning('Warning exists')
    # logger.info('Finish')
    logger = get_logger()
    logger.info("这个是我的测试logger日志代码")


