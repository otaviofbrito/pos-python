from abc import ABC, abstractmethod


class CalculadoraFinanceira(ABC):

    @abstractmethod
    def calcularMontanteComJuros(self, montanteInicial, periodoMeses, jurosAoMes):
        pass
