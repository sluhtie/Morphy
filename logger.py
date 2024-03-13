"""
===============================================================================

File: logger.py

 (C) 2024 by ADVANCED Systemhaus GmbH. All rights reserved.
             Maria Worona <maria.worona@advanced.info>

    2024.03.12 initial setup

    Python Version: 3.11.2
    UTF-8
    CRLF

===============================================================================
"""

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
