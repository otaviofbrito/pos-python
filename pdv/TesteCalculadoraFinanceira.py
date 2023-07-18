from pdv.dominio.servicos import CalculadoraFinanceira, CalculadoraJurosCompostos, CalculadoraJurosSimples
from pdv.dominio.servicos.CalculadoraJurosCompostos import CalculadoraJurosCompostos
from pdv.dominio.servicos.CalculadoraJurosSimples import CalculadoraJurosSimples

montanteInicial = 10000
periodoMeses = 3
jurosAoMes = 0.05

calculadora = CalculadoraJurosCompostos()
print("************* Cálculo de juros com calculadora de juros compostos **********************")
print("Montante inicial..:", montanteInicial)
print("Período em meses...:", periodoMeses)
print("Juros ao mês......:", jurosAoMes)
print("Objeto calculadora..:", calculadora)
print("Total..:", calculadora.calcularMontanteComJuros(montanteInicial, periodoMeses, jurosAoMes))
print("*****************************************************")

calculadora = CalculadoraJurosSimples()
print("************* Cálculo de juros com calculadora de juros simples  **********************")
print("Montante inicial..:", montanteInicial)
print("Período em meses...:", periodoMeses)
print("Juros ao mês......:", jurosAoMes)
print("Objeto calculadora..:", calculadora)
print("Total..:", calculadora. calcularMontanteComJuros(montanteInicial, periodoMeses, jurosAoMes))
print("*****************************************************")
