from pdv.dominio import TipoCalculadora
from pdv.dominio.pagamento.Pagamento import Pagamento
import pdv.dominio.servicos.CalculadoraJurosSimples
from pdv.dominio.servicos.CalculadoraJurosCompostos import CalculadoraJurosCompostos
from pdv.dominio.servicos.IJuros import IJuros


class PagamentoCartao(Pagamento, IJuros):

    def __init__(self, quantia, operadora, quantidadeParcelas, tipoCalculadora):
        super().__init__(quantia)
        self._operadora = operadora
        self._quantidadeParcelas = quantidadeParcelas

        if tipoCalculadora == TipoCalculadora.JUROS_SIMPLES:
            self.calculadora = pdv.dominio.servicos.CalculadoraJurosSimples.CalculadoraJurosSimples()
        elif tipoCalculadora == TipoCalculadora.JUROS_COMPOSTOS:
            self.calculadora = CalculadoraJurosCompostos()

    def simularParcelas(self, quantia, quantidadeParcelas):
        juros = self.consultarTaxaJuros()
        montanteComJuros = self.calculadora.calcularMontanteComJuros(quantia, quantidadeParcelas, juros)
        return montanteComJuros / quantidadeParcelas

    def consultarTaxaJuros(self):
        taxaJuros = 0.0
        if self._quantidadeParcelas == 2:
            taxaJuros = 2.5
        elif self._quantidadeParcelas == 3:
            taxaJuros = 5.0
        return taxaJuros

    def __str__(self):
        return "Tipo de pagamento...: Cartão de Crédito\n" \
            + super().__str__() + "\n" \
            + "Operadora................: " + str(self._operadora) + "\n" \
            + "Quantidade de parcelas....: " + str(self._quantidadeParcelas) + "\n" \
            + "Valor de cada parcela...: " + str(
                self.simularParcelas(super().getQuantiaFornecida(), self._quantidadeParcelas)) + "\n" \
            + "Tipo de calculadora usada na transação................: " + str(self.calculadora) + "\n"
