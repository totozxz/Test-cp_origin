from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from controller import controller
from model import body
app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "status_code": 422,
            "status": "failed",
            "detail": "wrong data type or missing some value"
            }
        )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/vat-calculation")
async def vat_calculation(cal: body):
    if (cal.price == 0 or cal.amount == 0):
        return JSONResponse(
            status_code=400,
            content={
                "status_code": 400,
                "status": "failed",
                "detail": "Price and Amount must not be 0"
                }
            )
    data = await controller.calculation(cal)
    return {
        "status_code": 200,
        "status": "success",
        "data": data
        }