from pdv.dominio.Endereco import Endereco
from pdv.dominio.Registradora import Registradora


class Loja:

    def __init__(self, nome, endereco: Endereco):
        self._nome = nome
        self._vendas = []
        self._registradoras = []
        self._endereco = endereco
        
        r1 = Registradora("R01")
        r2 = Registradora("R02")
        r3 = Registradora("R03")
        
        self.adicionarRegistradora(r1)
        self.adicionarRegistradora(r2)
        self.adicionarRegistradora(r3)
    
    def adicionarVenda(self, venda):
        self._vendas.append(venda)
    
    def adicionarRegistradora(self, registradora):
        self._registradoras.append(registradora)
    
    def getUltimaVenda(self):
        return self._vendas[-1]
    
    def getRegistradora(self, id):
        for registradora in self._registradoras:
            if registradora.getId() == id:
                return registradora
        return None
    
    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome
    
    def getEndereco(self):
        return self._endereco
    
    def setEndereco(self, endereco):
        self._endereco = endereco
