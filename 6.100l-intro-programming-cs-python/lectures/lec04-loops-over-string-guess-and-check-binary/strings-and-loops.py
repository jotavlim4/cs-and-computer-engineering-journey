# esse exemplo mostra três formas diferentes
# de percorrer os caracteres de uma string usando
# loop for.

s = "demo loops - fruit loops"
# usando indices dos caracteres da string
for index in range(len(s)):
    if s[index] == 'u' or s[index] == 'i':
        print("there is an i or u")
        
# usando o operador 'in':
for char in s:
    if char == 'u' or char == 'i':
        print("there is an i or u")

for char in s:
    if char in 'iu':
        print("there is an i or u")
        
