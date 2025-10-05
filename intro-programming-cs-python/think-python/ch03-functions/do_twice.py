def do_twice(f, v):
	f(v)
	f(v)

def print_spam():
	print('spam')

def print_twice(str):
	print(str)
	print(str)

def do_four(f, arg):
	do_twice(f, arg)
	do_twice(f, arg)

#1
#do_twice(print_spam)

#2
do_twice(print, 'do_twice com argumento')

#3
do_twice(print_twice, 'spam')

#5
do_four(print, 'spam')