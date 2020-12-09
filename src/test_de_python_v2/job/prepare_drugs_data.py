from test_de_python_v2.common.utils import normalize_column
import pandas as pd


def prepare_drugs(df:pd.DataFrame):
    '''
      Generate a well formated dataframe from drugs data
      @parameter : df
      @return : df_without_duplicate
      '''

    #we normalize all columns and we suppose that atccode values has the right format
    df_with_normalize_atccode = normalize_column(df, 'atccode')
    df_with_normalize_drug = normalize_column(df_with_normalize_atccode, 'drug')

    # sorting by atccode
    df_sort_by_atccode = df_with_normalize_drug.sort_values("atccode")

    # dropping duplicate rows
    df_without_duplicate = df_sort_by_atccode.drop_duplicates()

    return df_without_duplicate