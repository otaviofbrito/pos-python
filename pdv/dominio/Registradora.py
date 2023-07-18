from datetime import datetime

from pdv.dominio import TipoCalculadora
from pdv.dominio.CatalogoProdutos import CatalogoProdutos
from pdv.dominio.Venda import Venda
from pdv.dominio.pagamento import Operadora


class Registradora:

    def __init__(self, id):  # construtor da classe
        self._id = id
        self._vendas = []
        self._catalogo = CatalogoProdutos()

    def criarNovaVenda(self):
        venda = Venda(datetime.now())
        self._vendas.append(venda)

    def entrarItem(self, id, quantidade):
        descricaoProduto = self._catalogo.getDescricaoProduto(id)
        venda = self.getVendaCorrente()
        venda.criarItemVenda(descricaoProduto, quantidade)

        # raise exception

    def finalizarVenda(self):
        self.getVendaCorrente().setEstaCompleta(True)

    def fazerPagamentoDinheiro(self, quantiaFornecida):
        return self.getVendaCorrente().fazerPagamentoDinheiro(quantiaFornecida)

    def fazerPagamentoCheque(self, quantiaFornecida, banco):
        self.getVendaCorrente().fazerPagamentoCheque(quantiaFornecida, banco)

    def fazerPagamentoCartao(self, quantiaFornecida, operadora: Operadora, quantidadeParcelas,
                       tipoCalculadora: TipoCalculadora):
        self.getVendaCorrente().fazerPagamentoCartao(quantiaFornecida, operadora, quantidadeParcelas, tipoCalculadora)

    def getVendaCorrente(self):
        return self._vendas[-1]

    def getCatalogo(self):
        return self._catalogo

    def setCatalogo(self, catalogo):
        self._catalogo = catalogo

    def getId(self):
        return self._id
