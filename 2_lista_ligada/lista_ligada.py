
from no import No

class Lista_Ligada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0

    def adicionar(self, item):
        """ Adiciona no fim da lista. análises de custo O(n)"""

        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def exibir(self):
        """ Retorna os itens da lista em uma string. análises de custo O(n)"""

        itens = []
        no_atual = self.primeiro

        while no_atual:
            itens.append(str(no_atual.item))
            no_atual = no_atual.proximo

        return " -> ".join(itens) + (" -> null" if itens else "null")

    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. análises de custo O(n)"""

        atual = self.primeiro

        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo

        return False

    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. análises de custo O(n)"""

        if posicao < 0 or posicao >= self.tamanho:
            return None

        atual = self.primeiro
        indice = 0

        while indice < posicao:
            atual = atual.proximo
            indice += 1

        return atual.item

    def inserir(self, posicao, item):
        """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. análises de custo O(n)"""

        if posicao < 0 or posicao > self.tamanho:
            return False

        novo_no = No(item)

        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            indice = 0

            while indice < posicao - 1:
                atual = atual.proximo
                indice += 1

            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1
        return True

    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. análises de custo O(n)"""

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.primeiro = self.primeiro.proximo
        else:
            atual = self.primeiro
            indice = 0

            while indice < posicao - 1:
                atual = atual.proximo
                indice += 1

            atual.proximo = atual.proximo.proximo

        self.tamanho -= 1
        return True

    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. análises de custo O(n)"""

        if self.primeiro is None:
            return False

        if self.primeiro.item == item:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
            return True

        atual = self.primeiro

        while atual.proximo:
            if atual.proximo.item == item:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True

            atual = atual.proximo

        return False
