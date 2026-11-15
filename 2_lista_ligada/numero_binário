from pilha import Pilha


def decimal_para_binario(numero):

    if numero < 0:
        raise ValueError("O número deve ser inteiro e não negativo.")

    if numero == 0:
        return "0"

    pilha = Pilha()

    while numero > 0:
        resto = numero % 2
        pilha.empilhar(resto)
        numero = numero // 2

    binario = ""
    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario


if __name__ == "__main__":
    entrada = int(input("Digite um número decimal: "))
    print(f"{entrada} em binário: {decimal_para_binario(entrada)}")
