import time

def timer(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(end - start)
	return wrapper

@timer
def mytest(f):
	time.sleep(f)

mytest(5)
