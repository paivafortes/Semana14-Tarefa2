#Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a posição que ele se encontra.

def cria_lista():
    lista = []
    for i in range(10):
        numeros = int(input())
        lista.append(numeros)

    return lista


def encontra_posicao(lista, elemento):

    for i in range(10):
        if lista[i] == elemento:
            return i


def maior_da_lista(lista):
    return max(lista)


def main():
    pass
if __name__=="__main__":
    main()
    lista = cria_lista()
    maior = maior_da_lista(lista)
    resultado = encontra_posicao(lista, maior)

    print(f'{lista}\n{maior}\n{resultado}')


if __name__ == "__main__":
    main()