opcao = 1

while opcao != 0:
    print('-- Inversor de String --')
    palavra = input('\nDigite uma palavra: ')
    palavraInvertida = ''

    for letra in palavra:
        palavraInvertida = letra + palavraInvertida

    print('\nPalavra invertida: ', palavraInvertida)


    opcao = int(input('Deseja continuar a consulta: \n1 - Sim \n0 - Não\n'))

print('Programa encerrado')
