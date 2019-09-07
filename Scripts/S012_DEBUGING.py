print('\n---------------raise exception---------------------')


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

print('\n---------------traceback---------------------')
import os
import traceback


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


try:
    spam()
except Exception as e:
    err_path = os.path.join(os.getcwd(), 'Sources')
    print('err_path', err_path)
    os.chdir(err_path)
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    print(str(e))
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

print('\n--------------Assertions----------------------')
try:
    podBayDoorStatus = 'open'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
    podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
except Exception as e:
    print(str(e))

print('\n-----------------logging Module-------------------')
import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')

print('\n--------------Logging Levels  ----------------------')
import logging

logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
