Class Pilhar:
  def __init__(self):
    self._elementos = lista_ligada()

  def push(self, item):
    self._elementos.inserir_inicio(item)

  def  peek(self):
    if self.is_empty(): return None
    return self._elementos.primeiro.item

  def is_empty(self):
    return self._elementos.vazia()
