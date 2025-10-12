""" Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’ """

birthday = input("type your birthday (on the follow way mm/dd/yyyy): ")
# usamos o fatiamento de string para criar uma substring 
# com o valor conveniente para o problema
print(f"you were born in the year {birthday[6:]}")