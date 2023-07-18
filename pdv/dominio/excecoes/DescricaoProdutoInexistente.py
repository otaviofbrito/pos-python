from builtins import Exception


class DescricaoProdutoInexistente(Exception):

    def __init__(self, mensagem, id):
        super().__init__(mensagem)
        self.__id = id

    def __str__(self):
        return super().__str__() + "\nID....: " + str(self.id)
