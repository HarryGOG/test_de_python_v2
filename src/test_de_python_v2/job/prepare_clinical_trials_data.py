import pandas as pd
from test_de_python_v2.common.fill_empty import fill_empty_id_method1, fill_empty_journal
from test_de_python_v2.common.utils import convert_column_date, normalize_column


def prepare_clinical(df:pd.DataFrame):
    '''
      Generate a well formated dataframe from clinical trial data
      @parameter : df
      @return : df_without_duplicate
      '''

    #Fill misssing value
    df_with_id = fill_empty_id_method1(df)
    df_with_journal = fill_empty_journal(df_with_id)

    #Formated date
    df_with_date_formated = convert_column_date(df_with_journal, "/", '%d %B %Y')

    #Normalize string columns
    df_with_normalized_columns = normalize_column(df_with_date_formated, 'scientific_title')
    df_with_normalized_columns2 = normalize_column(df_with_normalized_columns, 'journal')

    # sorting by id
    df_sort_by_id = df_with_normalized_columns2.sort_values("id")

    # dropping duplicate rows
    df_without_duplicate = df_sort_by_id.drop_duplicates()

    return df_without_duplicate


