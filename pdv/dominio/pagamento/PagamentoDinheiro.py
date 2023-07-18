from pdv.dominio.pagamento.Pagamento import Pagamento


class PagamentoDinheiro(Pagamento):

    def __init__(self, quantia):
        super().__init__(quantia)

    def __str__(self):
        return "Tipo de pagamento...: Dinheiro\n" + \
            super().__str__()
