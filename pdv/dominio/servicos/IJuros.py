from abc import ABC, abstractmethod


class IJuros(ABC):

    @abstractmethod
    def consultarTaxaJuros(self):
        pass
