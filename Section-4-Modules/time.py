import time as t

time_now = t.localtime()

print("Transaction completed at ", str(time_now.tm_hour) + "h " + str(time_now.tm_min) + "m")

time_at = t.time()

delivery_time = time_at + (86400 * 7)

print(t.localtime(delivery_time))

