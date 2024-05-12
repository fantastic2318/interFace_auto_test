import os

from loguru import logger

from Config.settings import LOG_PATH


class Log:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        format_ = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> ' \
                  '| <magenta>{process}</magenta>:<yellow>{thread}</yellow> ' \
                  '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'

        #logger.add(os.path.join(LOG_PATH, 'runtime_{time}.log'), format=format_, backtrace=True, diagnose=True)
        """
        
        根据框架的运行环境 判断 日志文件是否需要输出到文件
        CI运行 输入文件
        手动执行 仅输入到控制台
        需要一个环境变量作为入参
        """
        pass


    def debug(self, message):
        logger.debug(message)


    def info(self, message):
        logger.info(message)

    def error(self,message):
        logger.error(message)

    def warning(self, message):
        logger.warning(message)

    def exception(self, message):
        logger.exception(message)


log = Log()

if __name__ == '__main__':
    log = Log()
    log.debug('这是好消息')