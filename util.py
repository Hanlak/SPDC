import pandas as pd
from enumParser import DescriptionColumnName, KeywordRegex, CreditColumnName


def find_dividend_in_df(df, bank):
    """
    
    :param df: 
    :param bank: 
    :return: 
    """
    description = DescriptionColumnName[bank]
    credit_col = CreditColumnName[bank]
    keyword = KeywordRegex[bank].lower()
    df[description] = df[description].apply(lambda x: str(x).lower())
    df = df[df[description].str.contains(keyword, case=True)]
    df[credit_col] = df[credit_col].apply(lambda x: float(x))
    dividend = df[credit_col].sum()
    return dividend

