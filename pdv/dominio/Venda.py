from datetime import datetime

from pdv.dominio.TipoCalculadora import TipoCalculadora
from pdv.dominio.ItemVenda import ItemVenda
from pdv.dominio.pagamento.Operadora import Operadora
from pdv.dominio.pagamento.PagamentoCartao import PagamentoCartao
from pdv.dominio.pagamento.PagamentoCheque import PagamentoCheque
from pdv.dominio.pagamento.PagamentoDinheiro import PagamentoDinheiro
from pdv.dominio.DescricaoProduto import DescricaoProduto


class Venda:

    def __init__(self, data):

        self._itensVenda = []
        self._estaCompleta = False
        self._data = data
        self._pagamento = None



    def getItemQuantity(self):
        qtd = 0
        for item in self._itensVenda:
            qtd += item.getQuantidade()

        return qtd

    def criarItemVenda(self, desc: DescricaoProduto, quantidade):
        iv = ItemVenda(desc, quantidade)
        self._itensVenda.append(iv)

    def fazerPagamentoDinheiro(self, quantiaFornecida):
        self._pagamento = PagamentoDinheiro(quantiaFornecida)
        return self.calcularTroco()

    def fazerPagamentoCheque(self, quantiaFornecida, banco):
        self._pagamento = PagamentoCheque(quantiaFornecida, banco)

    def fazerPagamentoCartao(self, quantiaFornecida, operadora: Operadora, quantidadeParcelas,
                       tipoCalculadora: TipoCalculadora):
        self._pagamento = PagamentoCartao(quantiaFornecida, operadora, quantidadeParcelas, tipoCalculadora)

    def calcularTroco(self):
        return self._pagamento.getQuantiaFornecida() - self.calcularTotalVenda()

    def calcularTotalVenda(self):
        totalVenda = 0.0
        for itemVenda in self._itensVenda:
            if itemVenda is not None:
                totalVenda += itemVenda.getdescricaoProduto().getPreco() * itemVenda.getQuantidade()
        return totalVenda

    def setEstaCompleta(self, estaCompleta):
        self.estaCompleta = estaCompleta

    def __str__(self):
        status = "completa" if self.estaCompleta else "incompleta"
        dataTemp = f"{self._data.day}/{self._data.month}/{self._data.year}"
        horaTemp = f"{self._data.hour}:{self._data.minute}:{self._data.second}"
        cabecalho = f"Data: {dataTemp} hora: {horaTemp}\n" \
                    f"\t\t\t\t\tStatus da venda: {status}\n\n" \
                    " Descrição\t\tPreço Unitário(R$)\t\tQuantidade\t\tSubtotal(R$) \n"
        corpo = ""
        for iv in self._itensVenda:
            if iv is not None:
                corpo += str(iv)
        rodape = f"Total à vista (R$)\t\t\t\t\t\t\t{self.calcularTotalVenda()}\n\n" \
                 f"{str(self._pagamento)}"
        return cabecalho + corpo + rodape
