"""
ABOUT
  This module is intended to be used for logging purposes in other programs.
  It provides a clean wrapping for the python-provided *logging* module.

HOW TO USE:
  import ez.log as logging
  log = logging.setup()
  log.set_level(logging.DEBUG)
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


import logging as _logging

### logging levels
DEBUG    = _logging.DEBUG
INFO     = _logging.INFO
WARNING  = _logging.WARNING
ERROR    = _logging.ERROR
CRITICAL = _logging.CRITICAL


def setup(format='%(asctime)s %(module)s %(levelname)s %(message)s', level=INFO):
    _logging.basicConfig(format=format, level=level)
    return _logging.getLogger()


def set_level(lvl):
    """
    Set the logging level.
    This should only be called once at the top level

    @param lvl (LEVEL): a logging level
    @return (Logger)
    """

    logger = _logging.getLogger()
    logger.setLevel(lvl)


def _message(lvl, msg, *args, **kws):
    # name = kws.pop('name', 'root')
    logger = _logging.getLogger()
    logger.log(lvl, msg, *args, **kws)

def debug(*args, **kws):
    _message(DEBUG, *args, **kws)

def info(*args, **kws):
    _message(INFO, *args, **kws)

def warn(*args, **kws):
    _message(WARNING, *args, **kws)

def error(*args, **kws):
    _message(ERROR, *args, **kws)

def critical(*args, **kws):
    _message(CRITICAL, *args, **kws)

