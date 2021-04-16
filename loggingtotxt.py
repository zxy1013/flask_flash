import logging

logger = logging.getLogger( )
logger.setLevel('DEBUG')

BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)

# 输出到控制台的handler
chlr = logging.StreamHandler( )
chlr.setFormatter(formatter)
chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level

# 输出到文件的handler
fhlr = logging.FileHandler('log/log.txt')
fhlr.setFormatter(formatter)

# 添加两个流
logger.addHandler(chlr)
logger.addHandler(fhlr)

# 设置log内容
logger.debug("Do something")
logger.info("Start print log")
logger.warning("Something maybe fail.")
logger.info("Finish")


# 文件
'''2021-04-15 18:11:35:DEBUG:Do something
2021-04-15 18:11:35:INFO:Start print log
2021-04-15 18:11:35:WARNING:Something maybe fail.
2021-04-15 18:11:35:INFO:Finish'''

# 控制台
'''2021-04-15 18:11:35:INFO:Start print log
2021-04-15 18:11:35:WARNING:Something maybe fail.
2021-04-15 18:11:35:INFO:Finish'''