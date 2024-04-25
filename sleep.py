import time
import sys
file = open ('/home/gian/Documents/learn/python/output.txt', 'a')
sys.stdout = file
t = 20

print ("Time to sleep: ", t, " seconds.")
print ("------Start------")

i=1
while i<=t:
    print(i)
    i += 1
    time.sleep(1)
print ("------Finish------")
file.close()
