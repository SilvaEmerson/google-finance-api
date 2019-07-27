import os


FORMULA_PREFIX = "=GOOGLEFINANCE"


def build_formula(stock_cod, exchange):
    return '{}("{}:{}")'.format(FORMULA_PREFIX, exchange, stock_cod)


def add_action(service, cell, stock_cod=None, exchange=None):
    formula = {
            'values': [[build_formula(stock_cod, exchange)]]
            }

    print(formula)
    return service.values().update(
            spreadsheetId=os.getenv('SPREADSHEET_ID'),
            range=cell,
            valueInputOption='USER_ENTERED',
            body=formula).execute()
