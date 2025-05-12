from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from api import logger, mongodb
from api.router import api_router


app = FastAPI()
app.include_router(api_router)
app.add_middleware(CORSMiddleware,
                   allow_origins=["https://mlr.gdmseeds.com",
                                  "http://localhost:3000",
                                  "http://127.0.0.1:3000",
                                  "http://0.0.0.0:3000"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.add_middleware(TrustedHostMiddleware,
                   allowed_hosts=["*.z13.web.core.windows.net",
                                  "*.azurewebsites.net",
                                  "*.ngrok.io",
                                  "*.gdmseeds.com",
                                  "localhost",
                                  "127.0.0.1",
                                  "0.0.0.0"])


if __name__ == "__main__":
    import uvicorn

    logger.info("Init app")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
