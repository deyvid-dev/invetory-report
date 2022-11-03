from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(product_list):
        estoque_empresa = []
        empresas_list = []
        string = ""

        for produto in product_list:
            estoque_empresa.append(produto["nome_da_empresa"])

        for nome in estoque_empresa:
            count_empresas = estoque_empresa.count(nome)
            empresas_list.append(dict(name=nome, count=count_empresas))

        counter = Counter(estoque_empresa)

        for empresa, quant in counter.items():
            string += f'- {empresa}: {quant}\n'

        simple_report = SimpleReport.generate(product_list)

        return (
            f'{simple_report}\n'
            f'Produtos estocados por empresa: \n'
            f'{string}'
        )
