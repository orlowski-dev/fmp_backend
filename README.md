# fmp_backend

## env file
```bash
DEBUG=
SECRET_KEY=
SERVER_URI=
CORS_ALLOWED_ORIGINS=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

## build and run

```
docker build <image_name> .
docker run --name <container_name> -p 8000:8000 --network <postgres_network> --env-file ./.env -d <image_name>
```
