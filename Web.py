import redis
import threading
import requests
import os


REDIS_URL = os.environ['REDISCLOUD_URL']
REDIS_CHAN = 'firebase'

class Listener(threading.Thread):
	def __init__(self, r, channels):
		threading.Thread.__init__(self)
		self.redis = r
		self.pubsub = self.redis.pubsub()
		self.pubsub.subscribe(channels)


	def work(self, item):
		print("Item recived {}").format(item)



	def run(self):
		for item in self.pubsub.listen():
			if item['data'] == "KILL":
				self.pubsub.unsubscribe()
				print(self, "unsubsribed")
				break
			else:
				self.work(item)

if __name__ == '__main__':

	r = redis.from_url(REDIS_URL)
	client = Listener(r, [REDIS_CHAN])
	client.start()
