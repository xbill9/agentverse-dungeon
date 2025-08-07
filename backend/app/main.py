import uuid
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from .api import router as api_router
from .crud import game_db

app = FastAPI(title="Boss Fight Dungeon")

# CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only the frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api")

# Serve frontend
try:
    app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")
except RuntimeError:
    print("Frontend build not found. Run `npm run build` in the `frontend` directory.")


@app.on_event("shutdown")
def shutdown_event():
    # Clean up mock database on shutdown if needed
    game_db.clear()
    print("Server shutting down. Game database cleared.")

