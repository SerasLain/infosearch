import logging
from showtime import mymodule


def main():
    """
    The main entry point of the application
    """

    logger = logging.getLogger("shwotime")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = mymodule.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()
