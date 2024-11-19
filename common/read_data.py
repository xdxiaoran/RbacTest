import os

import yaml
import json
from configparser import ConfigParser
from common.logger import logger

'''
对yaml、json、ini等文件进行数据读取
'''
class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info(f"读到数据 ==>>  {data} ")
        return data

    def load_json(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

data = ReadFileData()

if __name__ == '__main__':
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    INI_PATH = os.path.join(BASE_PATH, "config","setting.ini")
    data.load_ini(INI_PATH)
