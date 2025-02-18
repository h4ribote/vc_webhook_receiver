from fastapi import FastAPI, Request, status
import uvicorn
import api
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import config

app = FastAPI()
app.include_router(api.router)

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

if __name__ == "__main__":
    uvicorn.run(app, host=config.Server.HOST, port=config.Server.PORT, log_level="debug")
