import logging
import sys

LOGGER_LIST = None

def get_logger(name="ctp", level=logging.DEBUG):
    '''
    return handle to logger, initialize only once
    :param name:
    :param level:
    :return:
    '''
    global LOGGER_LIST

    if not LOGGER_LIST:
        LOGGER_LIST = set('_invalid_name_')

    if LOGGER_LIST and name in LOGGER_LIST:
        return logging.getLogger(name)
    else:
        LOGGER_LIST.add(name)

        logger = logging.getLogger(name)
        logger.setLevel(level)

        # redirect output to stdout as well
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger
