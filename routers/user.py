from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user_schemas import User


user_router = APIRouter()



@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@correo.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
