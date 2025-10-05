def check_fermat(a, b, c, n):
	message_1 = 'Holy smokes, Fermat was wrong!'
	message_2 = "No, that doesn´t work"
	if n > 2 and (a**n + b**c == c**n):
		print(message_1)
	else:
		print(message_2)


def test_check_fermat():
	a = int(input("Type a value for 'a'\n"))  
	b = int(input("Type a value for 'b'\n"))  
	c = int(input("Type a value for 'c'\n"))  
	n = int(input("Type a value for 'n'\n"))  
	check_fermat(a, b, c, n)  

test_check_fermat()  