from fastapi import FastAPI
from routers.generate_tutorial import router
import uvicorn

app = FastAPI()

# Include router in FastAPI app
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
