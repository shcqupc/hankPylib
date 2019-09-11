print('\n----------------The time Module cProfile--------------------')
import time
import cProfile as cp

print(time.time())

'''
def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
prod = 0
cp.run('prod = calcProd()')
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

print('\n--------------time.sleep()----------------------')
for i in range(5):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
print(time.time())
'''
print('\n---------------datetime Module---------------------')
import datetime

print(datetime.datetime.now())
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

print('\n----------------timedelta --------------------')
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
dt = datetime.datetime.now()
dt = dt + delta
print(dt)

print('\n---------------Converting ---------------------')
'''
%Y 	  Year with century, as in '2014'  
%y 	  Year without century, '00' to '99' (1970 to 2069)  
%m 	  Month as a decimal number, '01' to '12'  
%B 	  Full month name, as in 'November'  
%b 	  Abbreviated month name, as in 'Nov'  
%d 	  Day of the month, '01' to '31'  
%j 	  Day of the year, '001' to '366'  
%w 	  Day of the week, '0' (Sunday) to '6' (Saturday)  
%A 	  Full weekday name, as in 'Monday'  
%a 	  Abbreviated weekday name, as in 'Mon'  
%H 	  Hour (24-hour clock), '00' to '23'  
%I 	  Hour (12-hour clock), '01' to '12'  
%M 	  Minute, '00' to '59'  
%S 	  Second, '00' to '59'  
%p 	  'AM' or 'PM'  
%% 	  Literal '%' character
'''
dt = datetime.datetime.now().strftime('%Y/%B/%d %I:%M:%S%p %A')
print(dt)
dt = datetime.datetime.strptime('2019/September/11 11:16:32PM Wednesday', '%Y/%B/%d %I:%M:%S%p %A')
print(dt)

print('\n---------------Multithreading---------------------')
import threading
import time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap())
threadObj.start()

# threadObj1 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# threadObj1.start()

print('End of program.')
