from fastapi import FastAPI

app = FastAPI(title="DockerExample API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running in Docker!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
