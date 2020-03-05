import logging,logging.handlers
import os

def init_logging():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    st = logging.StreamHandler()
    ht = logging.handlers.TimedRotatingFileHandler(BASE_DIR+"/log/ihrm.log",when="S",interval=10,backupCount=3,encoding="utf-8")

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    st.setFormatter(formatter)
    ht.setFormatter(formatter)

    logger.addHandler(st)
    logger.addHandler(ht)



# main是在本页面运行先执行，在页面外调用本页面不执行
if __name__ == '__main__':
    init_logging()
    logging.info("测试app页面")
