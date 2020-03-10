'''
Created on 23.02.2020

@author: rafa
'''
from tkinter import filedialog
import pandas as pd
import logging

DEBUG = True
user_eingabe = 'j'
secondary_excel_filenames = []


def main(user_eingabe='j'):
    """
    Read Excelfiles
    :param:
    :return:
    """
    logging.info("Programmstart")
    print("Bitte Hauptexceldatei angeben")
    main_excel_file = filedialog.askopenfilename(initialdir="C:\ProgrammierungGIT\ExcelManipulator"
                                              , title="Select A File"
                                              , filetypes=(("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"),))
    df_main_excel = pd.read_excel(main_excel_file)
    logging.debug(df_main_excel.head())
    print("Bitte weitere Exceldateien angeben")
    secondary_excel_files = filedialog.askopenfilenames(initialdir="C:\ProgrammierungGIT\ExcelManipulator"
                                              , title="Select A File"
                                              , filetypes=(("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"),))
    logging.debug(secondary_excel_files)

    while user_eingabe == 'j':
        print("Eingelesene Excelfiles: ")
        for secondary_excel_file in secondary_excel_files:
            print(secondary_excel_file.rsplit('/', 1)[-1].lower())
        logging.debug(secondary_excel_files)

        in_filename = input("\nGebe Dateiname ein:  \n").lower()
        logging.debug(in_filename)
        excel_files = list(map(lambda x: x.rsplit('/', 1)[-1].lower()
                               , secondary_excel_files))
        if in_filename not in \
           list(map(lambda x: x.rsplit('/', 1)[-1].lower()
                    , secondary_excel_files)):
            print("Dateiname nicht gefunden")
        else:
            print("Exceldatei wird eingelesen")
            logging.debug(excel_files.index(in_filename))
            df_secondary_excel = pd.read_excel(
                secondary_excel_files[excel_files.index(in_filename)])
            df_secondary_excel = df_secondary_excel.fillna('')
            logging.debug(df_secondary_excel.head())
            print("Waehle Spaltennamen aus Spaltennamenliste (Nummer eintippen):")
            df_columns = list(df_secondary_excel.columns)
            for count, column in enumerate(df_columns):
                print("{}: {}".format(count, column))
            while True:
                try:
                    column_index = int(input("Bitte Zahl eingeben: "))
                except ValueError:
                    print("Das war keine Zahl")
                else:
                    break
            logging.debug("column_index: {}".format(column_index))
            print(df_columns)
            print(df_columns[column_index])
            secondary_column_name = df_columns[column_index]
            print(df_secondary_excel[secondary_column_name])
            df_main_columns = list(df_main_excel.columns)
            print("Waehle Spaltennamen aus Spaltennamenliste zum Ersetzen \
                   aus Hauptexcel (Nummer eintippen):")
            for count, column in enumerate(df_main_columns):
                print("{}: {}".format(count, column))
            while True:
                try:
                    column_index = int(input("Bitte Zahl eingeben: "))
                except ValueError:
                    print("Das war keine Zahl")
                except IndexError:
                    print("Bitte Spaltenzahl aus angegebener Liste eingeben")
                else:
                    break
            main_column_name = df_main_columns[column_index]
            df_main_excel[main_column_name] = df_secondary_excel[secondary_column_name]
            print(df_main_excel)
        user_eingabe = input("Weitere Dateinamen angeben (j/n)? \n")
        logging.debug(user_eingabe)

    with pd.ExcelWriter('output.xlsx') as writer:
        df_main_excel.to_excel(writer, sheet_name='Sheet_name_1', index=False)


if __name__ == '__main__':
    if DEBUG:
        LOGLEVEL = logging.DEBUG
    else:
        LOGLEVEL = logging.INFO

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)  
    main()
