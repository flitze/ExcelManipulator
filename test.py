'''
Created on 23.02.2020

@author: rafa
'''
import pandas as pd


def main():
    """
    """
    df = pd.read_excel("C:\ProgrammierungGIT\ExcelManipulator\JSON_EOF.xlsx")
    print(df)
    df_json = df[df.element_name.str.startswith('JSON_')].copy()
    df_json['trimmed_name'] = df_json.element_name \
                                     .apply(lambda x: x.split("JSON_")[-1])
    print(df_json)
    df_eof = df[df.element_name.str.startswith('EOF_')].copy()
    df_eof['trimmed_name'] = df_eof.element_name \
                                   .apply(lambda x: x.split("EOF_")[-1])
    print(df_eof)
    unique_jsons = df_json.trimmed_name.unique()
    print(unique_jsons)
    df_eof_2 = df_eof[~df_eof.trimmed_name.isin(unique_jsons)]
    print(df_eof_2)


if __name__ == '__main__':
    main()
