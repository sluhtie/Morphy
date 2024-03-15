import logging


def setup_logger():
    # Create logger
    logger_ = logging.getLogger(__name__)
    logger_.setLevel(logging.DEBUG)

    # Create file handler and set formatter
    formatter = logging.Formatter('[%(name)s][%(asctime)s@%(module)s:%(lineno)d] %(levelname)s - %(message)s')
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # Add the file handler to the logger
    logger_.addHandler(fh)

    return logger_


# Initialize the logger
logger = setup_logger()
