def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def print_cross():
	print('+ - - -', end = ' ')

def print_post():
	print('|       ', end = '')

def print_plus_row():
	do_twice(print_cross)
	print('+')

def print_post_row():
	do_twice(print_post)
	print('|')

def print_grid():
	print_plus_row()
	do_four(print_post_row)

def print_complete_grid():
	do_twice(print_grid)
	print_plus_row()

def print_plus_row_4x4():
	do_four(print_cross)
	print('+')

def print_post_row_4x4():
	do_four(print_post)
	print('|')

def print_grid_4x4():
	print_plus_row_4x4()
	do_four(print_post_row_4x4)

def print_grid_4x4_complete():
	do_four(print_grid_4x4)
	print_plus_row_4x4()
#1 
print_complete_grid()

print()

#2
print_grid_4x4_complete()