from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from models.models import Post, Comment

from sqlalchemy.orm import Session

from utils.auth import validate_token

router = APIRouter(prefix="/post")

class CreatePostRequest(BaseModel):
    title: str
    content: str

@router.post("/")
async def create_post(request: Request, create_post_request: CreatePostRequest, token_data: dict = Depends(validate_token)):
    """
    Create a post
    """
    
    with Session(request.app.state.db) as session:
        post = Post(
            title=create_post_request.title,
            content=create_post_request.content,
            user_id=token_data["user_id"]
        )
        session.add(post)
        session.commit()

    return JSONResponse(
        status_code=200,
        content={"message": "Post created"}
    )

class CreateCommentRequest(BaseModel):
    content: str
    post_id: int

@router.post("/comment")
async def create_comment(request: Request, create_comment_request: CreateCommentRequest, token_data: dict = Depends(validate_token)):
    """
    Create a comment
    """
    
    with Session(request.app.state.db) as session:
        comment = Comment(
            content=create_comment_request.content,
            user_id=token_data["user_id"],
            post_id=create_comment_request.post_id
        )
        session.add(comment)
        session.commit()

    return JSONResponse(
        status_code=200,
        content={"message": "Comment created"}
    )