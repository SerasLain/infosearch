# log_with_config.py
import logging
import logging.config
from showtime import mymodule2


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    logging.config.fileConfig('logconfig')
    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = mymodule2.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()
