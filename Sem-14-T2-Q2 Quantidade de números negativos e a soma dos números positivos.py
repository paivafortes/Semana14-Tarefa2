#Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de números negativos e a soma dos números positivos dessa lista.

def cria_lista():
    lista = []
    for i in range(10):
        numeros = int(input())
        lista.append(numeros)

    return lista


def numeros_negativos(lista):
    numeros_negativos = 0
    for i in range(10):
        if lista[i] < 0:
            numeros_negativos += 1

    return numeros_negativos

def soma_numeros_positivos(lista):
    soma_numeros_positivos = 0
    for i in range(10):
        if lista[i] > 0:
            soma_numeros_positivos += lista[i]

    return soma_numeros_positivos

def main():
    pass
if __name__=="__main__":
    main()
    lista = cria_lista()
    negativos = numeros_negativos(lista)
    soma_positivos = soma_numeros_positivos(lista)

    print(f'{lista}\n{negativos}\n{soma_positivos}')

if __name__ == "__main__":
    main()