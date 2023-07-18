from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, quantiaFornecida):
        self.quantiaFornecida = quantiaFornecida

    def getQuantiaFornecida(self):
        return self.quantiaFornecida

    def setQuantiaFornecida(self, quantia):
        self.quantiaFornecida = quantia

    def __str__(self):
        return "Quantia Fornecida: R$ " + str(self.quantiaFornecida)
