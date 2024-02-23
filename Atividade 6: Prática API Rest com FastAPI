from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class CurrencyConversionRequest(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

@app.get("/datetime")
def get_datetime():
    current_datetime = datetime.now()
    return {"datetime": current_datetime}

@app.post("/convert_currency")
def convert_currency(request: CurrencyConversionRequest):
    # Simulando uma conversão de moeda fixa (apenas para fins de exemplo)
    conversion_rate = 1.5  # Exemplo: 1 unidade da moeda de origem = 1.5 unidades da moeda de destino
    converted_amount = request.amount * conversion_rate
    return {"converted_amount": converted_amount, "currency": request.to_currency}

@app.get("/perform_operation")
def perform_operation(
    x: float = Query(..., description="Primeiro número"),
    y: float = Query(..., description="Segundo número"),
    operation: str = Query(..., description="Operação a ser realizada: add, subtract, multiply, divide")
):
    result = None
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = x / y
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Use add, subtract, multiply, or divide.")
    
    return {"result": result}

@app.post("/example_post")
def example_post(data: dict):
    # Exemplo simples de rota que aceita dados por meio de POST
    return {"received_data": data}
