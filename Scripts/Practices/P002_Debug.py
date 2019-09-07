print('\n--------------1.assert----------------------')


def fnc_1():
    spam = int(input())
    print(spam)
    assert spam >= 10, "less than 10"


fnc_1()

print('\n--------------Logging Levels  ----------------------')
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.WARNING)
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
