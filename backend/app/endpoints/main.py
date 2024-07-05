from fastapi import APIRouter

from app.endpoints.routes import account, basket, login, product, category, user


api_router = APIRouter()


api_router.include_router(account.router,  tags=["account"])
api_router.include_router(product.router,  tags=["product"])
api_router.include_router(category.router, tags=["category"])
api_router.include_router(basket.router,   tags=["basket"])
api_router.include_router(login.router,    tags=["login"])
api_router.include_router(user.router,     tags=["user"])
