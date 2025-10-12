""" Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect. """

largest = None
count = 0

while count < 10:
    number = int(input())
    if number % 2 == 1 and (largest is None or number > largest):
        largest = number
    count = count + 1
    
if largest is None:
    print("no odd number was entered")
else:
    print(f"{largest} is the largest odd number entered.")
    
    
# "(largest is None or number > largest):" lógica utilizada
# quando queremos comparar algo onde uma variável foi inicializa com True.