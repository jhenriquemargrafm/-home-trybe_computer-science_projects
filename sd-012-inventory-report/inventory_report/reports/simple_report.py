from datetime import datetime


class SimpleReport:
    made = 'Data de fabricação mais antiga:'
    valid = 'Data de validade mais próxima:'
    company = 'Empresa com maior quantidade de produtos estocados:'

    def oldest_fabrication_date(reports):
        dates = []
        for report in reports:
            dates.append(report['data_de_fabricacao'])
        return min(dates)

    def valid_date(reports):
        current_date = datetime.today().strftime('%Y-%m-%d')
        dates = []
        for report in reports:
            if report['data_de_validade'] > current_date:
                dates.append(report['data_de_validade'])
        return min(dates)

    def most_stocked_company(reports):
        companies = []
        for report in reports:
            companies.append(report['nome_da_empresa'])
        return max(companies)

    @classmethod
    def generate(cls, reports):
        report_valid_date = cls.valid_date(reports)
        report_oldest_fabrication_date = cls.oldest_fabrication_date(reports)
        report_most_stocked_company = cls.most_stocked_company(reports)
        return (
            f"{cls.made} {report_oldest_fabrication_date}\n"
            f"{cls.valid} {report_valid_date}\n"
            f"{cls.company} {report_most_stocked_company}\n"
        )
