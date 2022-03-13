from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(stock):
        simple_report_result = SimpleReport.generate(stock)
        companies = [company['nome_da_empresa'] for company in stock]
        companies_products = Counter(companies)  # [{ company: 4, company: 3 }]
        text = ''
        for key, value in companies_products.items():
            # items() permite acessar a chave e valor de um dicionário
            text += f'- {key}: {value}\n'
        complete_report = (
            f'{simple_report_result}'
            f'\nProdutos estocados por empresa: \n'
            f'{text}'
        )
        return complete_report
