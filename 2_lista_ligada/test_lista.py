
from lista_ligada import Lista_Ligada


def test_lista_vazia():
    lista = Lista_Ligada()

    assert lista.tamanho == 0
    assert lista.primeiro is None


def test_adicionar():
    lista = Lista_Ligada()

    lista.adicionar(10)

    assert lista.tamanho == 1
    assert lista.primeiro.item == 10


def test_adicionar_varios():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.tamanho == 3
    assert lista.primeiro.item == 10
    assert lista.primeiro.proximo.item == 20
    assert lista.primeiro.proximo.proximo.item == 30


def test_pesquisar_existente():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)

    assert lista.pesquisar(20) == True


def test_pesquisar_inexistente():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)

    assert lista.pesquisar(50) == False


def test_obter():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.obter(0) == 10
    assert lista.obter(1) == 20
    assert lista.obter(2) == 30


def test_obter_posicao_invalida():
    lista = Lista_Ligada()

    lista.adicionar(10)

    assert lista.obter(5) is None
    assert lista.obter(-1) is None


def test_inserir():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(30)

    assert lista.inserir(1, 20) == True
    assert lista.obter(0) == 10
    assert lista.obter(1) == 20
    assert lista.obter(2) == 30


def test_inserir_posicao_invalida():
    lista = Lista_Ligada()

    lista.adicionar(10)

    assert lista.inserir(5, 20) == False


def test_remover():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.remover(1) == True
    assert lista.obter(0) == 10
    assert lista.obter(1) == 30
    assert lista.tamanho == 2


def test_remover_posicao_invalida():
    lista = Lista_Ligada()

    lista.adicionar(10)

    assert lista.remover(5) == False


def test_remover_item():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.remover_item(20) == True
    assert lista.tamanho == 2
    assert lista.obter(1) == 30


def test_remover_item_inexistente():
    lista = Lista_Ligada()

    lista.adicionar(10)

    assert lista.remover_item(50) == False
