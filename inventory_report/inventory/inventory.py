import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, encoding="utf-8") as file:
            lista = list(csv.DictReader(file))

        if type == "simples":
            return SimpleReport.generate(lista)

        elif type == "completo":
            return CompleteReport.generate(lista)
