#Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn). Por exemplo, para as duas listas X e Y a seguir:

def cria_lista():
    lista = []
    for i in range(5):
        numeros = int(input())
        lista.append(numeros)
    return lista


def produto_escalar(lista_um, lista_dois):

    produto = 0

    for i in range(5):
        produto += lista_um[i] * lista_dois[i]

    return produto


def main():
    pass
if __name__=="__main__":
    main()
    lista1 = cria_lista()
    lista2 = cria_lista()

    resultado = produto_escalar(lista1, lista2)

    print(f'{lista1}\n{lista2}')
    print(f'({lista1[0]} x {lista2[0]}) + ({lista1[1]} x {lista2[1]}) + ({lista1[2]} x {lista2[2]}) + ({lista1[3]} x {lista2[3]}) + ({lista1[4]} x {lista2[4]}) = {resultado}')

if __name__ == "__main__":
    main()