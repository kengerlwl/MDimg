# coding=utf-8
import json
import os
import logging
#当前文件目录路径
FileDir = os.path.abspath(os.path.dirname(__file__))

# 返回上一级目录到根目录
FileDir = FileDir + '/..'

def get_config(run_env=None):
    # 读取配置文件
    if run_env is None:
        run_env = 'para'
    if 'SERVICE_ENV' in os.environ:
        run_env = os.environ['SERVICE_ENV']
    config_path = '{}/{}.json'.format(os.path.split(os.path.abspath(__file__))[0], run_env)
    # print(config_path)
    config_path = 'Config/para.json'
    if os.path.isfile(config_path):
        config_data = open(config_path, "r", encoding="utf-8").read()
        app_config = json.loads(config_data)  # 师兄的

        app_config["RUN_ENV"] = run_env
        return app_config
    else:
        logging.error("Config not exist")
        exit()
