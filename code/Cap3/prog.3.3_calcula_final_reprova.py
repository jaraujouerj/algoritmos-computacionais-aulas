nota1 = float(input("Qual é a primeira nota? "))
nota2 = float(input("E a segunda nota? "))
media = (nota1 + nota2)/2
print ("A média é ", media)
if media < 7:
    if media < 4:
        print ("Ficou reprovado :(")
    else:
        print ("Ficou para prova final")
else:
    print ("Passou direto!")
