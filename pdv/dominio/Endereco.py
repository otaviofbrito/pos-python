class Endereco:

    def __init__(self, logradouro, complemento, numero, cidade, bairro, uf, cep):
        
        self.logradouro = logradouro
        self.complemento = complemento
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.uf = uf
        self.cep = cep

    def getLogradouro(self):
        return self.logradouro

    def setLogradouro(self, logradouro):
        self.logradouro = logradouro

    def getComplemento(self):
        return self.complemento

    def setComplemento(self, complemento):
        self.complemento = complemento

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getBairro(self):
        return self.bairro

    def setBairro(self, bairro):
        self.bairro = bairro

    def getUf(self):
        return self.uf

    def setUf(self, uf):
        self.uf = uf

    def getCep(self):
        return self.cep

    def setCep(self, cep):
        self.cep = cep
