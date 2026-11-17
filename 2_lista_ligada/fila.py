from lista_ligada import ListaLigada

class Fila:
  def __init__(self):
    self._elementos = ListaLigada()

  def Enfileirar(self, item):
    self._elementos.inserir_fim(item)

  def Dequeue(self):
    return self._elementos.remover_inicio()

  def 
