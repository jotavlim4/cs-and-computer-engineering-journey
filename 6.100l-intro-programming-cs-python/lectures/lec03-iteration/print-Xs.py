""" Replace the comment in the following code with a
while loop. """

num_x = int(input('How many times should I print the letter X? '))
to_print = ''
count = 0
while count < num_x:
    to_print = to_print + 'X'
    count = count + 1
print(to_print)