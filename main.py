from routes import routers

import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)