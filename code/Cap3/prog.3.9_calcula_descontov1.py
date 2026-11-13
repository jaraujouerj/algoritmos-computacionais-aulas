idade = int(input('Qual a idade? '))
if idade >= 0 and idade < 12:
    print ('Desconto é de 100%')
elif idade >= 12 and idade < 26:
    print ('Desconto é de 50%')
else:
    print ('Sem Desconto')
