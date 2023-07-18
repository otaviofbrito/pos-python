from pdv.dominio.Endereco import Endereco
from pdv.dominio.Loja import Loja
from pdv.dominio.excecoes import DescricaoProdutoInexistente
from pdv.dominio import TipoCalculadora
from pdv.dominio.pagamento.Operadora import Operadora

def main():


    try:

        endereco = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
        loja = Loja("Supermercado Preço Bão", endereco)

        registradora = loja.getRegistradora("R01")
        registradora.criarNovaVenda()

        registradora.entrarItem("01", 3)
        registradora.entrarItem("02", 2)
        registradora.entrarItem("03", 1)

        registradora.finalizarVenda()

        totalVenda = registradora.getVendaCorrente().calcularTotalVenda()
        registradora.fazerPagamentoCartao(totalVenda, Operadora.AMERICAN.value, 1, TipoCalculadora.JUROS_SIMPLES)

    # 0.0 é o troco a ser devolvido
        gerarRecibo(registradora, 0.0)

    # Criando uma venda com pagamento em dinheiro na segunda registradora
        registradora2 = loja.getRegistradora("R02")
        registradora2.criarNovaVenda()

        registradora2.entrarItem("06", 3)
        registradora2.entrarItem("10", 2)
        registradora2.entrarItem("07", 10)

        registradora2.finalizarVenda()

        totalVenda3 = registradora2.getVendaCorrente().calcularTotalVenda()

        registradora2.fazerPagamentoDinheiro(100)

        gerarRecibo(registradora2, 100 - totalVenda3)

        registradora3 = loja.getRegistradora("R03")
        registradora3.criarNovaVenda()

        registradora3.entrarItem("06", 3)
        registradora3.entrarItem("07", 2)
        registradora3.entrarItem("02", 1)
        registradora3.finalizarVenda()

        totalVenda2 = registradora3.getVendaCorrente().calcularTotalVenda()
        registradora3.fazerPagamentoCartao(totalVenda2, Operadora.AMERICAN.value, 1, TipoCalculadora.JUROS_SIMPLES)

        gerarRecibo(registradora3, 0.0)

    except DescricaoProdutoInexistente as d:
        print(d.getMessage())

def gerarRecibo(registradora, troco):
    venda = registradora.getVendaCorrente()
    print("")
    print("--------------------------- Supermercado Preço Bão ---------------------------")
    print("                             Registradora : " + registradora.getId())
    print("\t\t\t\tCUPOM FISCAL")
    print(venda)
    print("Troco................: R$ " + str(troco))


if __name__ == "__main__":
    main()
