import pandas as pd
import re

def find_similar_id(scientific_title:str, date:str, df:pd.DataFrame):
    '''
    Find similar id. Two articles are consider as similar id, if they have the same 'scientific_title', and 'date'
    @parameter : scientific_title
    @parameter date
    @parameter : df (the clinical data)
    @return : id
    '''
    for index, row in df.iterrows():
        if(scientific_title==row['scientific_title'] and date==row["date"] and row['id']!=''):
            return row['id']

    return "No match"


def fill_empty_id_method1(df:pd.DataFrame):
    '''
     Fill empty id. using find_similar_id method
     @parameter : df (the clinical data)
     @return : df (with non empty id)
     '''
    for index, row in df.iterrows():
        if (row['id'] == ''):
            id = find_similar_id(row['scientific_title'], row['date'], df)
            row['id'] = id

    return df


def find_similar_journal(scientific_title:str, date:str, df:pd.DataFrame):
    '''
    Find similar journal. Two articles are consider as similar journal, if they have the same 'scientific_title', and 'date'
    @parameter : scientific_title
    @parameter date
    @parameter : df (the clinical data)
    @return : id
    '''
    for index, row in df.iterrows():
        if(scientific_title==row['scientific_title'] and date==row["date"] and row['journal']!=''):
            return row['journal']

    return "No match"


def fill_empty_journal(df:pd.DataFrame):
    '''
     Fill empty journal. using find_similar_journal method
     @parameter : df (the clinical data)
     @return : df (with non empty id)
     '''
    for index, row in df.iterrows():
        if (row['journal'] == ''):
            journal = find_similar_journal(row['scientific_title'], row['date'], df)
            row['journal'] = journal

    return df


def extract_int(string_with_int:str):
    '''
     Extract int from a string
     @parameter : string_with_int
     @return : id (in int)
     '''
    result = re.search('([0-9]+)', str(string_with_int))

    if result:
        id = int(result.group(1))
    else:
        id = int(0)

    return id


def formated_id_column(df:pd.DataFrame):
    '''
     Convert id to int and fill empty rows
     @parameter : df
     @return : df (with non empty id)
     '''
    df['id'] = df['id'].apply(extract_int)

    return df


def fill_empty_id_method2(df:pd.DataFrame):
    '''
     Fill empty id . To fill empty row, we increase the last id number
     @parameter : df (the clinical data)
     @return : df (with non empty id)
     '''
    df_formated_id = formated_id_column(df)
    globals()['max_id']  = df_formated_id['id'].max()

    def get_max():
        globals()['max_id'] = globals()['max_id'] + 1
        return  globals()['max_id']

    df_formated_id['id'] = df_formated_id['id'].apply(lambda x: x if(x !=0) else get_max())

    return df_formated_id