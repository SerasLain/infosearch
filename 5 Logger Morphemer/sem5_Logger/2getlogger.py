import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    # raise RuntimeError
    print('a' + 2)
# except RuntimeError:
except Exception as e:
    # log.error(e, exc_info=True)
    # log.error(e)
    log.exception(e)

if __name__ == '__main__':
    pass
