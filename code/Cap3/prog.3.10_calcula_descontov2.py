idade = int(input('Qual a idade? '))
if  0 <= idade < 12:
    print ('Desconto é de 100%')
elif 12 <=  idade < 26:
    print ('Desconto é de 50%')
else:
    print ('Sem Desconto')
