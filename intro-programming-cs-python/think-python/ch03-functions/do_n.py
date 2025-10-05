def do_n(f, n):
	if n <= 0:
		return
	else:
		f(n)
		do_n(f, n-1)

do_n(print, 10)