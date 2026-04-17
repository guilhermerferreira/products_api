from fastapi import FastAPI, status

from products_api.routers import users, brands, products


app = FastAPI()


app.include_router(
    router=users.router,
    prefix='/api/v1/users',
    tags=['users'],
)

app.include_router(
    router=brands.router,
    prefix='/api/v1/brands',
    tags=['brands'],
)

app.include_router(
    router=products.router,
    prefix='/api/v1/products',
    tags=['products'],
)


@app.get(path='/', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'ok'}

