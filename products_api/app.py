from fastapi import FastAPI, status

from products_api.routers import users


app = FastAPI()


app.include_router(
    router=users.routers,
    prefix='/api/v1/users',
    tags=['users']
)


@app.get(path='/', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'ok'}

