# ********************************************************************************************************
import time
# ********************************************************************************************************
print(time.ctime(0))        # convert a time expressed in seconds since epoch to a readable string
#                               epoch = when your computer thinks time begun (reference point)
print(time.time())          # return current seconds since epoch
print(time.ctime(time.time()))  # will get current time

# ********************************************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime()  # local time
# time_object = time.gmtime() # UTC time
# local_time = time.strftime("", time_object)
# print(local_time)

# time_object = time.localtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2024"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)