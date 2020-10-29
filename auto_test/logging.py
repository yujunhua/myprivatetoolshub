import logging
import time


class Demolog:


    def log(self):
        # 创建一个日志器
        logger = logging.getLogger("logger")
        # 设置日志输出最低等级
        logger.setLevel(logging.INFO)
        # 创建处理器
        shHandler = logging.StreamHandler()
        fhHandler = logging.FileHandler(filename="{}_log".format(time.strftime("%Y_%m_%d_%H_%M_%S_",time.localtime())),
                                        encoding="utf-8")
        # 创建一个格式器
        formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s", datefmt="%Y/%m/%d/%X")

        shHandler.setFormatter(formator)
        fhHandler.setFormatter(formator)
        logger.addHandler(shHandler)
        logger.addHandler(fhHandler)
        return logger
        # logger.debug("debug信息")
        # logger.info("info信息")
        # logger.warning("warning信息")
        # logger.error("error信息")
        # logger.critical("critical信息")

    def sum(self, a, b):
        try:
            sum = a + b
            self.log().info("正确计算出{} + {} 之和".format(a, b))
            return sum
        except Exception as error:
            self.log().error("{} + {} 之和计算错误:{}".format(a, b, error))

Demolog().sum("a", 2)