from pdv.dominio.DescricaoProduto import DescricaoProduto


class ItemVenda:

    def __init__(self, descricaoProduto: DescricaoProduto, quantidade):
        self._descricaoProduto = descricaoProduto
        self._quantidade = quantidade

    def getQuantidade(self):
        return self._quantidade

    def getdescricaoProduto(self):
        return self._descricaoProduto

    def getSubtotal(self):
        return self._quantidade * self._descricaoProduto.getPreco()

    def __str__(self):
        return str(self._descricaoProduto) + "\t  " + str(self._quantidade) + "   \t\t" + str(self.getSubtotal()) + '\n'
