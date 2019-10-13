import logging
from showtime import mymodule


def main():
    """
    The main entry point of the application
    """

    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = mymodule.add(7, 8)
    logging.info("Done!")


if __name__ == "__main__":
    main()
