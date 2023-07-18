from pdv.dominio.DescricaoProduto import DescricaoProduto
from pdv.dominio.excecoes.DescricaoProdutoInexistente import DescricaoProdutoInexistente


class CatalogoProdutos:

    def __init__(self):

        self.descricoesProdutos = []
        self.contadorDescricoesProdutos = 0

        d1 = DescricaoProduto("01", 3.75, "Chocolate Talento")
        d2 = DescricaoProduto("02", 1.50, "Chiclete Trident")
        d3 = DescricaoProduto("03", 2.50, "Lata de Coca-cola")
        d4 = DescricaoProduto("04", 2.00, "Agua Mineral Caxambu")
        d5 = DescricaoProduto("05", 5.99, "Cerveja Corona extra")
        d6 = DescricaoProduto("06", 2.50, "Biscoito cream cracker")
        d7 = DescricaoProduto("07", 4.50, "Leite condensado")
        d8 = DescricaoProduto("08", 18.00, "Cafe Prima Qualitat")
        d9 = DescricaoProduto("09", 2.00, "Danete")
        d10 = DescricaoProduto("10", 1.00, "Bombril")

        self.descricoesProdutos.append(d1)
        self.descricoesProdutos.append(d2)
        self.descricoesProdutos.append(d3)
        self.descricoesProdutos.append(d4)
        self.descricoesProdutos.append(d5)
        self.descricoesProdutos.append(d6)
        self.descricoesProdutos.append(d7)
        self.descricoesProdutos.append(d8)
        self.descricoesProdutos.append(d9)
        self.descricoesProdutos.append(d10)

    def getDescricaoProduto(self, id):
        for desc in self.descricoesProdutos:
            if id == desc.getId():
                return desc
        raise DescricaoProdutoInexistente("Descricao Inexistente para o produto", id)
