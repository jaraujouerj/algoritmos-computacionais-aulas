def palindromo(palavra):
    return palavra == palavra[::-1]
print(palindromo('ovo')) # True
print(palindromo('Ovo')) # False <- diferencia maiúsculas!



