from fastapi import FastAPI

from pydantic import BaseModel


class InputDataScheme(BaseModel):
    num1: int | float
    num2: int | float


class ResponseDataScheme(BaseModel):
    result: int | float


app = FastAPI(
    title="FastAPI Lesson 3"
)


@app.post("/calculate", response_model=ResponseDataScheme)
async def calculate(data: InputDataScheme):
    return ResponseDataScheme(
        result=data.num1 + data.num2
    )
