import logging
sub_logger = logging.getLogger("main.sub")
def sub1():
    print("Hello This is sub1")
    sub_logger.debug("This is sub1")
