import logging
import logging.handlers
import os


def log_it(**kwargs):
    logger = logging.getLogger(kwargs['name'])
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    if kwargs.has_key('console'):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    elif kwargs.has_key('rotate'):
        rlh = logging.handlers.RotatingFileHandler(os.path.join(kwargs['logpath'], kwargs['logname']), maxBytes=102400, backupCount=100)
        rlh.setLevel(logging.DEBUG)
        rlh.setFormatter(formatter)
        logger.addHandler(rlh)
    else:
        logging.basicConfig(filename=os.path.join(kwargs['logpath'], kwargs['logname']), format='%(aasctime)s - %(name) - %(message)s')
    return logger

