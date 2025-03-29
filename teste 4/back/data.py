from fastapi import Depends
from typing import Annotated
import pandas as pd

#dependency function to open csv file and return dataframe
def get_data():
    df = pd.read_csv("./files/Relatorio_cadop.csv", delimiter=';', encoding='utf-8')
    yield df

#dependency to access dataframe (using this dependency the file is only loaded when the server receives a request and don't use memory to keep the file opened all the time)
DataDep = Annotated[pd.DataFrame, Depends(get_data)]