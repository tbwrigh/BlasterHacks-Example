from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from models.models import User

import hashlib

from sqlalchemy.orm import Session

import jwt


router = APIRouter(prefix="/user")

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: Request, login_request: LoginRequest):
    """
    Login a user
    """
    
    with Session(request.app.state.db) as session:
        user = session.query(User).filter(User.email == login_request.email).first()
        if not user:
            return JSONResponse(
                status_code=400,
                content={"message": "User not found"}
            )
        
        hashed_password = hashlib.sha256(login_request.password.encode()).hexdigest()
        if user.password_hash != hashed_password:
            return JSONResponse(
                status_code=400,
                content={"message": "Invalid password"}
            )
        
        token = jwt.encode({
            "user_id": user.id,
            "email": user.email
        }, "secret", algorithm="HS256")

    return JSONResponse(
        status_code=200,
        content={"token": token}
    )


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register(request: Request, register_request: RegisterRequest):
    """
    Register a new user
    """
    
    # Check if the email already exists for a user
    with Session(request.app.state.db) as session:
        user = session.query(User).filter(User.email == register_request.email).first()
        if user:
            return JSONResponse(
                status_code=400,
                content={"message": "Email already exists"}
            )
                
    # Create a new user
    with Session(request.app.state.db) as session:
        hashed_password = hashlib.sha256(register_request.password.encode()).hexdigest()
        user = User(
            name=register_request.username,
            email=register_request.email,
            password_hash=hashed_password
        )

        session.add(user)
        session.commit()
    
    return JSONResponse(
        status_code=200,
        content={"message": "User registered successfully"}
    )
        
