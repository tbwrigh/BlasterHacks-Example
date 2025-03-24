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

@router.get("/")
async def get_posts(request: Request):
    """
    Get all posts
    """
    
    with Session(request.app.state.db) as session:
        posts = session.query(Post).all()
        posts = [{
            "title": post.title,
            "content": post.content,
            "author": post.user.name,
            "post_id": post.id,
            "comments": [{
                "content": comment.content,
                "author": comment.user.name,
                "comment_id": comment.id
                } for comment in post.comments]
            } for post in posts]

    return JSONResponse(
        status_code=200,
        content={"posts": posts}
    )

@router.delete("/{post_id}")
async def delete_post(request: Request, post_id: int, token_data: dict = Depends(validate_token)):
    """
    Delete a post
    """

    with Session(request.app.state.db) as session:
        post = session.query(Post).filter(Post.id == post_id).first()
        if not post:
            return JSONResponse(
                status_code=400,
                content={"message": "Post not found"}
            )
        
        if post.user_id != token_data["user_id"]:
            return JSONResponse(
                status_code=400,
                content={"message": "Unauthorized"}
            )

        session.delete(post)
        session.commit()

    return JSONResponse(
        status_code=200,
        content={"message": "Post deleted"}
    )

@router.delete("/comment/{comment_id}")
async def delete_comment(request: Request, comment_id: int, token_data: dict = Depends(validate_token)):
    """
    Delete a comment
    """

    with Session(request.app.state.db) as session:
        comment = session.query(Comment).filter(Comment.id == comment_id).first()
        if not comment:
            return JSONResponse(
                status_code=400,
                content={"message": "Comment not found"}
            )
        
        if comment.user_id != token_data["user_id"]:
            return JSONResponse(
                status_code=400,
                content={"message": "Unauthorized"}
            )

        session.delete(comment)
        session.commit()

    return JSONResponse(
        status_code=200,
        content={"message": "Comment deleted"}
    )