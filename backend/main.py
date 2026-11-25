from fastapi import FastAPI

app = FastAPI(
    title="OSV Watchlist API",  # Sets the API name.
    version="1.0.0"            # Sets the API version.
)

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the OSV Watchlist API",
        "status": "running",
        "version": app.version
    }