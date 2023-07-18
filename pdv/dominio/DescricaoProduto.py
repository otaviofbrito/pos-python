class DescricaoProduto:

    def __init__(self, id, preco, descricao):
        self.__id = id
        self.__preco = preco
        self.__descricao = descricao

    def getId(self):
        return self.__id

    def getPreco(self):
        return self.__preco

    def __str__(self):
        return self.__descricao + "\t\t" + str(self.__preco) + "\t"

    def __eq__(self, other):
        if isinstance(other, DescricaoProduto) and other is not None:
            return self.__id == other.getId()
        return False
