# reprodução de erros

print("Hello World!")

#omitindo um dos parenteses
# print("Hello World" -> SyntaxError: '(' was never closed

#imprimindo uma string sem omitindo uma ou ambas as strings
#print("Hello World) -> SyntaxError: unterminated string literal (detected at line 8)
#print(Hello World) -> SyntaxError: invalid syntax. Perhaps you forgot a comma?

#usando um sina de mais para indicar que um número é positivo durante uma soma
#print(2++2)  -> o resultado é o mesmo que print(2+2)

#usando zeros a esquerda de números
#print(02) -> SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

#dois valores sem nenhum operador entre eles:
#print(2 2) -> SyntaxError: invalid syntax. Perhaps you forgot a comma?