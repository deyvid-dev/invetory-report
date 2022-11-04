import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, type):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                lista = list(csv.DictReader(file))

        if path.endswith(".json"):
            with open(path) as file:
                lista = json.load(file)

        if path.endswith(".xml"):
            with open(path) as file:
                lista = xmltodict.parse(file.read())["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(lista)

        elif type == "completo":
            return CompleteReport.generate(lista)
