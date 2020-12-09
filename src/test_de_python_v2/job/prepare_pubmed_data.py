import pandas as pd
from test_de_python_v2.common.utils import convert_column_date_to_string, convert_column_date, normalize_column
from test_de_python_v2.common.fill_empty import fill_empty_id_method2


def prepare_pubmed(df_csv:pd.DataFrame, df_json:pd.DataFrame):
    '''
      Generate a well formated dataframe from pubmed data
      @parameter : df
      @return : df_without_duplicate
      '''
    #prepare data from the json file
    df_json_formated_date = convert_column_date_to_string(df_json)

    #prepare data from csv file
    df_csv['id'] = df_csv['id'].apply(str)
    df_csv_formated_date = convert_column_date(df_csv, "/", '%Y-%m-%d')

    #concatenate the two data sources
    df = pd.concat([df_csv_formated_date, df_json_formated_date])

    #Fill empty id
    df_with_filled_id = fill_empty_id_method2(df)

    # Normalize string columns
    df_with_prepared_title = normalize_column(df_with_filled_id, 'title')
    df_with_prepared_journal = normalize_column(df_with_prepared_title, 'journal')

    # sorting by id
    df_sort_by_id = df_with_prepared_journal.sort_values("id")

    # dropping duplicate rows
    df_without_duplicate = df_sort_by_id.drop_duplicates()

    return df_without_duplicate