
import logging as _logging

### logging levels
DEBUG    = _logging.DEBUG
INFO     = _logging.INFO
WARNING  = _logging.WARNING
ERROR    = _logging.ERROR
CRITICAL = _logging.CRITICAL


## defaults
_DEFAULT_NAME  = 'root'
_LOG_FORMAT    = '%(asctime)s %(module)s %(levelname)s %(message)s'
_DEFAULT_LEVEL = INFO

def setup(name=_DEFAULT_NAME, format=_LOG_FORMAT, level=_DEFAULT_LEVEL):
    """
    @param name (string)
    @param format (string)
    @param level (LEVEL)
    @return (Logger)
    """

    _logging.basicConfig(format=format, level=level)
    return _logging.getLogger(name)


def set_level(lvl, name=_DEFAULT_NAME):
    """
    Set the logging level.
    This should only be called once at the top level

    @param lvl (LEVEL): a logging level
    @param name='root' (string)
    """

    logger = _logging.getLogger(name)
    logger.setLevel(lvl)
