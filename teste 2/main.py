from tabula import read_pdf
import pandas as pd
from zipfile import ZipFile
import os

if __name__ == "__main__":

    # reads pdf file and create pandas dataframe from it
    df = pd.concat(
        read_pdf(
            "Anexo_I.pdf",
            pages="3-181",
            multiple_tables=False
        )
    )

    # stores column names from dataframe
    column_names = list(df.columns)

    cleaned_tables = []

    # each page of the pdf contains the header, so it's necessary to remove it from the dataframe
    for row in df.values:
        if list(row) != column_names:
            table_cleaned = pd.DataFrame([row], columns=column_names)
            cleaned_tables.append(table_cleaned)


    # creates a new dataframe without the additional headers
    df1 = pd.concat(cleaned_tables, ignore_index=True)

    # renames the columns to their full name
    df1.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

    # removes special characters from data
    df1.columns = df1.columns.str.replace('\r', ' ')
    df1 = df1.map(lambda x: str(x).replace('\r', ' ') if isinstance(x, str) else x)

    # file names to be saved
    file_name = "anexo_i.csv"
    zip_file_name = "Teste_Thiago_Fernandes.zip"

    # saves the dataframe as a csv file
    df1.to_csv(file_name, index=False, encoding='utf-8', sep=";")

    # creates a zip file containing the csv file
    with ZipFile(zip_file_name, 'w') as zipf:
        zipf.write(file_name, os.path.basename(file_name))