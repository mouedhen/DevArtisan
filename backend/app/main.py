from fastapi import FastAPI, HTTPException
from backend.app.exception_handlers import (
    http_exception_handler,
    integrity_error_handler,
    generic_exception_handler,
)
from sqlalchemy.exc import IntegrityError

app = FastAPI()

# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/error")
def create_error():
    raise HTTPException(status_code=404, detail="Resource not found")