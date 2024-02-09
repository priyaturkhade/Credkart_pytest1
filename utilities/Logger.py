import logging  # built in python


class LogGenerator:
    @staticmethod
    def loggen():
        # given path and file name
        logfile = logging.FileHandler("F:\\Pycharm projects\\Credkart_pytest1\\Logs\\credkart.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s  - %(funcName)s - %(lineno)s- %(message)s ")
        logfile.setFormatter(format)
        logger = logging.getLogger()
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# Debug
# info
# Warning
# Error
# Critical

# file info
# log format
# run log create
