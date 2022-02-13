import pandas as pd
from tabula.io import read_pdf


def read_sbi_statement(statement_io):
    """

    :param statement_io:
    :return:
    """
    tables = read_pdf(statement_io, pages='all')
    data = pd.concat(tables)
    return data

