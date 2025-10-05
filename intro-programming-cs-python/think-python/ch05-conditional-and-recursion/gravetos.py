def is_triangle(a, b, c):
	if a >= b + c or b >= a + c or c >= a + b:
		print('No')
	else:
		print('Yes')
def user_input():
	a = int(input())
	b = int(input())
	c = int(input())
	is_triangle(a, b, c)

#uma outra implementação:

def is_triangle_2(a, b, c):
	print('No' if a + b > c or a + c > b or b + c > a else 'Yes')

def user_input_2():
	a, b, c = map(int, input().split())
	is_triangle_2(a, b, c)

if __name__ == "__main__":
	user_input()
	user_input_2()