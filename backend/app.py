from pathlib import Path

from api.endpoints.calculate import router as calculate_router
from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates





# create app

app = FastAPI(title="WhichPlates API", description="Calculate required plates and set weights",)

root_router = APIRouter()
@root_router.get("/", status_code=200, tags=['Home'])
def home():
    return {"message": "home"}

app.include_router(calculate_router, prefix='/api')
app.include_router(root_router)


if __name__ == "__main__":
    
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")