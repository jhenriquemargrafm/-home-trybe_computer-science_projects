from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if (path.endswith('json')):
            stock = []
            with open(path) as file:
                stock_json = json.load(file)
                for elemento in stock_json:
                    stock.append(elemento)
            return stock
        else:
            raise(ValueError('Arquivo inválido'))
