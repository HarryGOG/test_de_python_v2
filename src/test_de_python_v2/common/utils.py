import unicodedata
from datetime import datetime
import pandas as pd
import re



def normalize_string(string_with_accent:str):
    '''
      Normalize a string
      @parameter : string_with_accent
      @return : str(text)
      '''
    text = unicodedata.normalize('NFD', string_with_accent.lower())\
                    .encode('ascii', 'ignore').decode("utf-8").strip()

    return str(text)


def normalize_column(df:pd.DataFrame, column_name:str):
    '''
      Normalize a string column
      @parameter : df
      @parameter : column_name
      @return : df (with the normalize column)
      '''
    df[column_name] = df[column_name].map(lambda x: re.sub(r'(\\x[a-zA-Z0-9]*)*', '', x))
    df[column_name] = df[column_name].map(lambda x: normalize_string(x))

    return df


def convert_to_date(string_with_full_month:str, input_date_format:str ='%d %B %Y'):
    '''
      Change the date format to %d/%m/%Y format
      @parameter : string_with_full_month
      @parameter : input_date_format
      @return : string
      '''
    # example '1 January 2020' , '2020-01-01'
    return datetime.strptime(string_with_full_month, input_date_format).strftime("%d/%m/%Y")


def check_date(date_string:str, check_string:str = "/"):
    '''
      Check if a character appear in a string
      @parameter : date_string
      @parameter : check_string
      @return : Boolean
      '''
    return  check_string in date_string


def prepare_date(date_string:str, check_good_date:str, input_date_format:str):
    '''
      Convert if necessary a string date to "%d/%m/%Y" format
      @parameter : date_string
      @parameter : check_good_date
      @parameter : input_date_format
      @return : string
      '''
    if check_date(date_string, check_good_date):
        return date_string
    else:
        return convert_to_date(date_string, input_date_format)


def convert_column_date(df:pd.DataFrame, check_good_date:str, input_date_format:str):
    '''
      Convert if necessary a string date column to "%d/%m/%Y" format
      @parameter : date_string
      @parameter : check_good_date
      @parameter : input_date_format
      @return : df
      '''
    df['date'] = df['date'].map(lambda x:  prepare_date(x, check_good_date, input_date_format))

    return df

def convert_column_date_to_string(df:pd.DataFrame, column_name:str='date'):
    '''
      Convert a date column to "%d/%m/%Y" format
      @parameter : df
      @parameter : column_name
      @return : df
      '''
    df[column_name] = df[column_name].map(lambda x:  x.strftime("%d/%m/%Y"))

    return df








# def remove_utf8_literal(string_with_nonASCII:str):
#
#     encoded_string = string_with_nonASCII.encode("ascii", "ignore")
#     clean_string = encoded_string.decode()
#
#     return clean_string



# def normalize_column(df:pd.DataFrame):
#
#     df['journal'] = df['journal'].apply(normalize_string)
#
#     #for index, row in df.iterrows():
#         #row[column_name] = normalize_string(row[column_name])
#      #   print(row[column_name], normalize_string(row[column_name]))
#
#     return df





# def prepare_clinical(path_clinical:str="tests/test_data/clinical_trials.csv"):
#     df = pd.read_csv(path_clinical, dtype=str).fillna('')
#     df['a'] = df['a'].apply(lambda x: x + 1)
#     normalize_string(string_with_accent: str)
#
#     #df['scientific_title'] = df['scientific_title'].apply(lambda x: normalize_string(x))
#     #df['journal'] = df['journal'].apply(lambda x: normalize_string(x))
#
#     return df


