from collections import Counter


class SimpleReport():
    def __init__(self, list):
        self.list = list

    def generate(list):
        data_fabricacao = []
        empresa = []
        data_validade = []

        for position in list:
            data_fabricacao.append(position["data_de_fabricacao"])
            empresa.append(position["nome_da_empresa"])
            data_validade.append(position["data_de_validade"])

        fabricacao_mais_antiga = min(data_fabricacao)
        validade_mais_prox = min(data_validade)

        counter = Counter(empresa)
        empresa_mais_prod = max(counter, key=empresa.count)

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_prox}\n"
            f"Empresa com mais produtos: {empresa_mais_prod}"
        )
