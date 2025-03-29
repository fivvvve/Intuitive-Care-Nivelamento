from fastapi import APIRouter, Response
from enum import Enum
from data import DataDep

#defines router for this file
router = APIRouter (
    tags=["dataframe search"]
)

#defines available values for type query param
class TypeEnum(str, Enum):
    registro_ans = "registro_ans"
    cnpj = "cnpj"
    modalidade = "modalidade"
    text = "text"

@router.get("/textual-search", summary="Searches the dataframe according to text received")
def search(text: str, type: TypeEnum, data: DataDep, response: Response):

    #transform text received to uppercase
    text = text.upper()

    #searchs for data in the pandas dataframe according to parameters received
    if type == 'registro_ans':
        result = data[data['Registro_ANS'].astype(str).str.contains(text)]
    elif type == 'cnpj':
        result = data[data['CNPJ'].astype(str).str.contains(text)]
    elif type == 'modalidade':
        result = data[data['Modalidade'].astype(str).str.upper().str.contains(text)]
    else:
        result = data[data['Razao_Social'].astype(str).str.contains(text) |
                  data['Nome_Fantasia'].astype(str).str.contains(text) |
                  data['Representante'].astype(str).str.contains(text)]
    
    #in case no data was found
    if not len(result):
        response.status_code = 404
        return "No data Found"
    
    #changes na values to empty string to send data
    result = result.fillna("")
    
    #return data in JSON format
    return result.to_dict(orient="records")
