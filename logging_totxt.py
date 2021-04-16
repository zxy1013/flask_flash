import logging

# 输出日志的级别 level=logging.WARNING 高于的显示 输出到log/log.txt文件中
logging.basicConfig(filename='log/log.txt', filemode='a', level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 级别 debug<info<warning<error 设置错误信息
logger.debug("Do something")
logger.info("Start print log")
logger.warning("Something maybe fail.")
logger.error('error')

# 2021-04-15 17:54:49,255 - __main__ - WARNING - Something maybe fail.
# 2021-04-15 17:54:49,255 - __main__ - ERROR - error