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
                return cls.import_type(type, lista)

        elif path.endswith(".json"):
            with open(path) as file:
                lista = json.load(file)
                return cls.import_type(type, lista)

        elif path.endswith(".xml"):
            with open(path) as file:
                lista = xmltodict.parse(file.read())["dataset"]["record"]
                return cls.import_type(type, lista)

    def import_type(type, list):
        if type == "simples":
            return SimpleReport.generate(list)

        elif type == "completo":
            return CompleteReport.generate(list)
