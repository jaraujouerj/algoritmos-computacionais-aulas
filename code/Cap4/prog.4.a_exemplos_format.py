nome, nota = ’Ana’, 8.456
print(’Aluno {} tirou {:.1f}’.format(nome, nota))
print(f’Aluno {nome} tirou {nota:.1f}’) # f-string
print(f’{nome:>10}|{nota:<8.2f}|{42:05d}’) # alinhamento e zeros
print(f’{0.256:.1%} {1234567:,}’) # 25.6% 1,234,567
print(f’{"Graus":>9}{"Seno":>9}’)
