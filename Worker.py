"""
Worker process-- sends initial information to the web app
Initially sends zero, adds one to recived input
"""
import redis
import json

from web import REDIS_URL, REDIS_CHAN
from time import sleep


r = redis.from_url(REDIS_URL)
num = 0
while(True):
	payload = json.dumps({
		'value': num,
		})
	r.publish(REDIS_CHAN, payload)
	num +=1
	sleep(1)
