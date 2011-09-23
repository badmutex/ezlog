"""
ABOUT
  This module is intended to be used for logging purposes in other programs.
  It provides a clean wrapping for the python-provided *logging* module.

HOW TO USE:
  import ez.log as log
  log.setup(__name__)
  log.set_level(log.DEBUG)
  ...
  log.debug('oops')
  log.info('hello')
  log.warn('uh oh...')
  log.error('mayday! mayday!')
  log.critical('42 / 0')

LEVELs:
  In order:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
"""


################################################################################
#                                                                              #
################################################################################


import logging



### module-level logger
_DEFAULT_LOGGER = None

def _get_logger():
    """
    Get the module-level logger
    @raise ValueError, if the logger has not yet been set
    """
    global _DEFAULT_LOGGER
    if _DEFAULT_LOGGER is None:
        raise ValueError, 'Module-level logger has not yet been set'
    return _DEFAULT_LOGGER

def _set_logger(logger):
    """set the module-level logger"""
    global _DEFAULT_LOGGER
    _DEFAULT_LOGGER = logger


### logging levels
DEBUG    = logging.DEBUG
INFO     = logging.INFO
WARNING  = logging.WARNING
ERROR    = logging.ERROR
CRITICAL = logging.CRITICAL



def make_logger(name, loggerLevel=INFO, handlerLevel=DEBUG, logformat='%(asctime)s %(name)s %(levelname)s %(message)s'):
    """
    @param name (string): a name for this logger
    @param loggerLevel=INFO (LEVEL): the minimum logging level for the logger
    @param handlerLevel=DEBUG (LEVEL): the minimum logging level the the handler
    @param logformat='%(asctime)s %(name)s %(levelname)s %(message)s' (str)
    @return (logging.Logger): a Logger from the python logger module for *name*
    """

    print 'name:', name

    logger    = logging.getLogger(name)
    logger.setLevel(loggerLevel)

    handler   = logging.StreamHandler()
    handler.setLevel(handlerLevel)

    formatter = logging.Formatter(logformat)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def setup(*args, **kws):
    """
    Sets up the module-level logger

    @params *args, **kws: passed to *make_logger*
    """
    logger = make_logger(*args, **kws)
    _set_logger(logger)



def set_level(lvl):
    """
    Set the logging level.
    This should only be called once at the top level

    @param logger (Logger)
    @param lvl (LEVEL): a logging level

    Example:
        log
        log.setup_logger(__name__)
        log.set_level(log.DEBUG)
    """

    logger = _get_logger()
    logger.setLevel(lvl)


def _message(lvl, msg, *args, **kws):
    logger = _get_logger()
    logger.log(lvl, msg, *args, **kws)

def debug(*args, **kws):
    _message(logging.DEBUG, *args, **kws)

def info(*args, **kws):
    _message(logging.INFO, *args, **kws)

def warn(*args, **kws):
    _message(logging.WARNING, *args, **kws)

def error(*args, **kws):
    _message(logging.ERROR, *args, **kws)

def critical(*args, **kws):
    _message(logging.CRITICAL, *args, **kws)

