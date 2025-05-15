from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle de données d'entrée
class Operation(BaseModel):
    nb1: float
    nb2: float
    op: str  # "+", "-", "*", "/"

@app.post("/calculer")
def calculer(operation: Operation):
    a, b, op = operation.nb1, operation.nb2, operation.op

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division par zéro non autorisée.")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Opération non reconnue. Utiliser +, -, *, ou /.")

    return {"résultat": result}
