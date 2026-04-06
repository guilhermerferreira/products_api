from fastapi import FastAPI, status

from products_api.routers import users, brands


app = FastAPI()


app.include_router(
    router=users.routers,
    prefix='/api/v1/users',
    tags=['users'],
)

app.include_router(
    router=brands.routers,
    prefix='/api/v1/brands',
    tags=['brands'],
)


@app.get(path='/', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'ok'}

