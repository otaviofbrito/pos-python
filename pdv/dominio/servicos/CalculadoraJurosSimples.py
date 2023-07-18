from pdv.dominio.servicos.CalculadoraFinanceira import CalculadoraFinanceira


class CalculadoraJurosSimples(CalculadoraFinanceira):

    def calcularMontanteComJuros (self, montanteInicial, periodoMeses, jurosAoMes):
        totalJuros = montanteInicial * periodoMeses * (jurosAoMes * 0.01)
        novoMontante = montanteInicial + totalJuros
        return novoMontante

    def __str__(self):
        return "Calculadora de juros simples"
