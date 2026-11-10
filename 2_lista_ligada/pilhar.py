from lista_ligada.listav3.lista_ligada import ListaLigada
Class Pilhar:
  def __init__(self):
    self._elementos = lista_ligada()

  def empilhar(self, item):
    self._elementos.inserir_inicio(item)

  def  topo(self):
    if self.is_empty(): return None
    return self._elementos.primeiro.item

  def vazia(self):
    return self._elementos.vazia()
    
  def desempilhar(self):
    return self._elementos.remover_inicio()
