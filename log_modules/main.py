import sub
import sub2
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("main")

def main():
    sub.sub1()
    logger.error("main debug")


if "__main__" == __name__:
    main()  