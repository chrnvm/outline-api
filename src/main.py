from fastapi import FastAPI
import uvicorn
from routers import *


app = FastAPI(
    title="Outline API",
    version="1.0",

    # disable documentation
    # docs_url=None,
    # redoc_url=None

)

app.include_router(all_keys_router)
app.include_router(key_router)
app.include_router(server_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3366, log_level="debug", reload=True)
