import json
import sys
#x='{"user":"test","timestamp":"2024-05-17 12:32:46","ticket_id":"1223213214214124213"}'
x=sys.argv[1]

print ("x is: " + x)

#parse json
y = json.loads(x)

print (y["user"])