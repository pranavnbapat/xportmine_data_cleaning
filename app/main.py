import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from routes import general_routes, file_routes
from starlette.responses import RedirectResponse

app = FastAPI()

# Include routes from other files
app.include_router(general_routes.router)
app.include_router(file_routes.router)


@app.get("/", include_in_schema=False)      # Exclude from OpenAPI docs
async def root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)

