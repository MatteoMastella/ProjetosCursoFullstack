
# maiúsculas e minúsculas
# símbolos e espaços

'''
Security = chave
5ecuryt1 = senha

'''

chave = input('Digite a base da sua senha: ')

senha = ""

for letra in chave:
    if letra in "Aa": senha += "4"
    elif letra in "Bb": senha += "O"
    elif letra in "Cc": senha += "##"
    elif letra in "Dd": senha += "Q"
    elif letra in "Ee": senha += "$"
    elif letra in "Ff": senha += "%"
    elif letra in "Gg": senha += "T"
    elif letra in "Hh": senha += "U"
    elif letra in "Ii": senha += "1"
    elif letra in "Jj": senha += "W"
    elif letra in "Kk": senha += "X"
    elif letra in "Ll": senha += "Y"
    elif letra in "Mm": senha += "Z"
    else: senha += letra
print(senha)


