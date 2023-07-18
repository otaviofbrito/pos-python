from pdv.dominio.pagamento.Pagamento import Pagamento


class PagamentoCheque(Pagamento):

    def __init__(self, quantiaFornecida, banco):
        super().__init__(quantiaFornecida)
        self._banco = banco

    def getBanco(self):
        return self._banco

    def setBanco(self, banco):
        self._banco = banco

    def __str__(self):
        return "Tipo de pagamento...: Cheque\n" + \
            "Quantia fornecida....: R$ {}\n".format(super().getQuantiaFornecida()) + \
            "Banco................: {}".format(self._banco)
