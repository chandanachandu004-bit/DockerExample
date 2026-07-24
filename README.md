# DockerExample

A minimal FastAPI application packaged for Docker.

## Run locally with Docker

Build and start the container:

```bash
docker build -t dockerexample .
docker run -p 8000:8000 dockerexample
```

Or use Docker Compose:

```bash
docker compose up --build
```

## Endpoints

- `GET /` → returns a greeting message
- `GET /health` → returns service health status

## Verify

After the container starts, open:

- http://localhost:8000/
- http://localhost:8000/health

