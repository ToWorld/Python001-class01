def func(x):
	return x ** 2

def mymap(func1, args):
	l = []
	for i in args:
		c = func1(i)
		l.append(c)
	print(l)

l1 = [1, 2, 3, 4]

mymap(func, l1)
