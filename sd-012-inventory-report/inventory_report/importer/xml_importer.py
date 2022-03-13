from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if (path.endswith('xml')):
            tree = ET.parse(path)
            root = tree.getroot()
            stock = [
                {elemento.tag: elemento.text for elemento in record}
                for record in root.findall('record')
            ]
            return stock
        else:
            raise(ValueError('Arquivo inválido'))
