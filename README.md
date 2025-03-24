# Welcome to the BlasterHacks 2025 Example Project

This project is meant to be a starting point for anyone who doesn't have experience coding. It will cover a bunch of topics to help you get started at this hackathon. While we would prefer this to be more a of areference for you to gain technical insights and tips as you build your own project, feel free to build this as your project with your own unique twists if you so choose.


Before we jump into building our demo project and learning about all the tools to hlpe you succeed I'd like to put a little disclaimer, this guide was written on a Mac. All tools, code, and tricks were tested on a Mac, so if you are on Windows or Linux be warned this isn't tested (but it should all still work).

Another disclaimer: This is designed as a hackathon project. It does not follow best practices for managing secrets, using secure passwords, CORS policies, login systems, etc. It is meant to be a quick and dirty method of getting a functional application.


Jump to any of the following sections:

- [Tools](#tools)
  - [Git](#git)
  - [Visual Studio Code](#visual-studio-code)
  - [Python](#python)
  - [Node.js](#nodejs)
  - [Docker (advanced)](#docker-advanced)
- [Project Set Up](#project-set-up)
  - [Making a Github Repo](#making-the-github-repository)
  - [Sharing the Repo](#sharing-the-repo)
  - [Cloning the Repo](#cloning-the-repo)
  - [Making Your First Commit](#lets-make-our-first-commits)
- [Docker Set Up (optional)](#docker-set-up-optional)
- [Coding the Backend](#coding-the-backend)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-our-dependencies)
  - [Our First Endpoint](#making-our-first-endpoint)
  - [Initialize Alembic](#initialize-alembic)
  - [Backend Docker Set Up](#set-up-docker-for-backend)
  - [Connecting to the DB](#connect-to-our-database)
  - [CORS](#dealing-with-cors)
  - [Our First Controller](#our-first-controller)
    - [Finishing /register](#finishing-register)
    - [Finishing /login](#finishing-login)
  - [Post and Comment Models](#post-and-comment-models)
  - [Set Up Post Controller](#set-up-the-post-controller)
    - [Checking Auth](#checking-auth)
    - [Get Posts](#get-post-endpoint)
- [Coding the Frontend](#coding-the-frontend)
  - [Expanding our Gitignore](#expanding-our-gitignore)
  - [Start Our SvelteKit Project](#start-our-sveltekit-project)

# Tools

Before we get started with our super cool project, there are some helpful tools that will set your team up for success.

## Git

Git is a source control tool that will allow you to share code and keep track of changes. We will have more information on using git further into the guide, for now let's just make sure it is installed. Follow the [official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for specific instructions on how to install git.

Once you have completed the instructions for your operating system, open a terrminal and run `git --version` to verify you have installed git.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

So long as you are on an up to date Windows 11 installation you should have WinGet available.

To install Git with WinGet run the following command from powershell:

```ps1
winget install -e --id Git.Git
```

</details>

<details> 
<summary>Mac</summary>

On Mac, installing form the terminal requires Homebrew which you need to install if you haven't already.

<details>
<summary>Install Homebrew</summary>

To install Homebrew run the following command from your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

</details>

Once you have Homebrew installed it is as simple as opening a terminal and running:

```bash
brew install git
```

</details>

<details> 
<summary>Linux</summary>

Assuming you are on a Debian Linux distribution run:

```bash
apt install git
```

If you are on another distribution family, find the relevant command for your package manager.

</details>



## Visual Studio Code

Visual Studio Code (VSCode) is going to be our text editory of choice. Download it from the [official site](https://code.visualstudio.com/download). While any text editor will do I think VSCode is arguably the best free text editor for development.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In Powershell run:

```ps1
winget install -e --id Microsoft.VisualStudioCode
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install --cask visual-studio-code
```

</details>

<details> 
<summary>Linux</summary>

First add the apt repository.

To manually install the apt repository run the following commands.

```bash
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
```

To automatically install the apt repository run:

```bash
echo "code code/add-microsoft-repo boolean true" | sudo debconf-set-selections
```

Then update our package cache and install our package:

```bash
sudo apt install apt-transport-https
sudo apt update
sudo apt install code # or code-insiders
```

</details>

## Python

For this project I used Python 3.12 but any version from 3.10 onwards should be perfectly fine. If you need to install a new copy of Python, definitely go for Python 3.13. That said the [Python downloads page](https://code.visualstudio.com/download) should have the most recent stable release for your system available to download right at the top of hte page.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In powershell run:

```ps1
winget install -e --id Python.Python.3
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install python
```

</details>

<details> 
<summary>Linux</summary>

In your terminal run:

```bash
sudo apt install python3 python3-pip
```

</details>

## Node.js

Node.js is a very useful tool for building frontend projects. We are going to use it in our example project as well. Install it from the [official website](https://nodejs.org/en/download).

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In powershell run:

```ps1
winget install -e --id OpenJS.NodeJS
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install node
```

</details>

<details> 
<summary>Linux</summary>

In your terminal run:

```bash
sudo apt install nodejs
```

</details>

## Docker (Advanced)

Docker is a really cool tool used in industry for consistency, security, and scalability. Throughout this tutorial I will show the development process of this project with and without Docker. Docker will make our lives easier in a lot of ways, but it is another layer of complexity, so while I'd reccomend following the tutorial with it, feel free to skip it. Download it from the [official website](https://www.docker.com/get-started/) by hitting the download docker desktop button.  

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In powershell run:

```ps1
winget install -e --id Docker.DockerDesktop
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install docker
```

</details>

<details> 
<summary>Linux</summary>

First uninstall any potential conflicting packages by running:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Then set up Docker's official apt repository:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Then install Docker:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

</details>

# Project Set Up

## Making the GitHub repository

On the Github Home Page hit the green new button.

![Github Add Button](reference-images/github-home.png)

Now fill out the creation screen.

![New Repo Form](reference-images/new-repo.png)

Make sure owner shows your name. Set a good name for your project, whether it be `BlasterHacks25` or something similar or the name of your actual project. Optionally add a description of your project. For the 3 sections below description, make sure your selections match mine: Public, Add a README file, and add .gitignore template: Python.

## Sharing the Repo

For the easiest time collaboration you will want to share the repo with your team. To do that that, from the repo home page, click the settings tab. 

In the settings tab, click collaborators on the left side menu. Then hit the add people button and search for your teammates github usernames.

![Share Repo button](reference-images/share-repo.png)

Now your teammates need to accept the invitation. To do that, they should go to their notifications tab in github, click on the invite notification, then accept the invitation.

![Notification Button](reference-images/notification-button.png)

![Notification List](reference-images/notification-list.png)

![Accept Invitation](reference-images/accept-invite.png)

Now our Repo is set up in GitHub.

## Cloning The Repo

If you just installed git, you will need to set up SSH keys to be able to interact with your repository.

<details>
<summary>Set Up SSH Keys for Github</summary>

Setting up SSH keys for GitHub isn't too hard.

First you need to generate SSH Keys, which GitHub already has a great write up on [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac). For this write up, make sure you select the tab for your operating system.

Second, once you have generated your SSH keys you need to add them to your GitHub account, which also has a thorough write up from GitHub [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

</details>

Now that you presumably have your keys, we need to the remote endpoint from GitHub. To do that, we will go to the repo's home page, click the green code button button, make sure we are on the SSH tab, and click the copy icon.

![Code Button](reference-images/code.png)

Now to clone the repo we are going to open a terminal (or Powershell in Windows) in our Documents folder. Then we will run:

```bash
git clone <SSH Reference>
```

In my case it is:

```bash
git clone git@github.com:tbwrigh/BlasterHacks-Example.git
```

## Let's Make Our First Commits

So we haev this fancy git repo, what now? Well we make changes and track them here. Let's start adding our names to the README.

First, let's open the repository in VSCode. Then open the README.md file and add your name.

Then open a terminal (I'd strongly reccomend utilizing the VSCode built in terminal. You can open it by hitting the new terminal option under the terminal menu for the application.), and run through the following processes.

### Staging Our Changes (git add)

The first step in tracking our changes is staging them. This prepares them to be committed but if we need to make additional changes we can here. Additionally we can choose to stage certain changes and not stage others. If we edited 2 files, we can stage one to be tracked. To do this we can run:

```bash
git add <filename>
```

If you want to stage everything run the following commands from the base folder of the repo.

```bash
git add .
```

So to stage just the README run:

```bash
git add README.md
```

### Commit the Changes (git commit)

Now that we have our README staged, we need to commit the change. This will save it in our repository as a tracked change. Additionally when we track our changes, we leave a message that can help us figure out what we did more quickly when we are looking back on our changes. To do this we will run:

```bash
git commit -m "<My Message>"
```

### Pushing the Change(s) (git push)

The whole point of GitHub is to share our code, so how does our team get these changes? We push them to GitHub. To do this we will run:

```bash
git push <remote> <branch>
```

By default, the remote for a repo is `origin` and the default branch is `main`. So our default command to push would be:

```bash
git push origin main
```

Fortunately, our defaults tend to be automatically picked up, so we should be able to just run:

```bash
git push
```


### Getting Other People's Changes

So now the changes are in GitHub but our teammates didn't automatically recieve the changes. To get the changes they need to pull. To do that, you can run:

```
git pull
```

Now, sometimes you might run into a small issue: a merge conflict. 

<details>

<summary>More About Merge Conflicts</summary>

Merge conflicts occur when you have committed a change locally and try to pull a change that conflicts with the change you have locally. You can resolve merge conflicts with VSCode. Resolving merge conflicts is often considered a challenge for beginners, but all you really have to do is look at the conflicting blocks of code and keep whatever parts you want. Sometimes you may want to keep parts of both, so you can delete some parts of each and keep parts of each. 

If you want more details about merge conflicts and resolving them, checkout [this video](https://www.youtube.com/watch?v=HosPml1qkrg).

</details>

# Docker Set Up (optional)

In the root of the repository make a file called `docker-compose.yml` and in it paste the following:

```yml
version: '3.9'

services:
  db:
    container_name: db
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"
    volumes:
      - db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 5s
      retries: 10
      start_period: 10s

volumes:
  db-volume:
```

This will set up docker compose with one container for PostgreSQL. We will add more to this later, but for now this is all the docker set up we need. 

For now, let's get this running as is. To start docker we can run:

```bash
docker compose up -d
```

# Coding the Backend

First, let's start by making a backend folder in the root of our repository. Additionally let's add a file called `main.py` inside the backend folder.

## Set up a Virtual Environment

Python uses Virtual Environments to manage dependencies for each project. In our backend folder we will want to run:

```bash
python3 -m venv venv
```

Then to activate the virtual environment is run the following command for your system.

<details>

<summary>For Linux or Mac</summary>

Run:

```bash
source venv/bin/activate
```

</details>

<details>

<summary>For Windows</summary>

Run:

```ps1
.\venv\bin\Activate.ps1
```

If you run into an issue but not being allowed to run powershell scripts, in an admin powershell run:

```ps1
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

</details>

## Install Our Dependencies

Our main web server will be built with FastAPI. To install FastAPI run:

```bash
pip install "fastapi[standard]"
```

We also will use SQLAlchemy and Alembic to manage our database. To install these we can run:

```bash
pip install sqlalchemy alembic
```

We will also use PyJWT to make and verify JWTs. To install it run:

```bash
pip install pyjwt
```

We should track our Python dependencies. To do that we can run:

```bash
pip freeze > requirements.txt
```

If we wanted to install the dependencies tracked in the requirements.txt we can run:

```bash
pip install -r requirements.txt
```

## Making Our First Endpoint

In our `main.py` we will add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Returns the API version
    """
    return {"API Version": "1.0.0"}
```

This will make it so that when we hit the `/` path on our server, we will get the response `{"API Version": "1.0.0"}`. 

To run our server we can run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then we can hit our API at `http://localhost:8000/`

## Initialize Alembic

We need to set up Alembic. We can do that by running the following command in the backend folder:

```bash
alembic init alembic
```

An folder called `alembic` will be created, in that folder open `env.py`. 

Under `from alembic import context` we should add:

```python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
from models import Base
```

Then we will find a line with `target_metadata = None` make that:

```python
target_metadata = Base.metadata
```

In the `alembic.ini` file we will set the `sqlalchemy.url`. 

If you are using Docker set it to:

```ini
sqlalchemy.url = postgresql://postgres:password@db/postgres
```

If you are not using Docker:

```ini
sqlalchemy.url = sqlite:///./app.db
```

Now we need to make a model for object we want to store in our database. For now let's just have a user model. Make models folder in the backend. Inside that models folder make a file called `models.py`. In it put the following contents:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
```

Now we need to make a migration. To do this run:

```bash
alembic revision --autogenerate -m "Initial migration"
```

To apply the migration, if we are not using Docker, then run:

```bash
alembic upgrade head
```

If we are using Docker, we will have composer handle running the migrations for us.

If you are not using Docker add the following line to your `.gitignore`:

```
*.db
```

## Set up Docker for Backend

In the backend folder make file called `Dockerfile` and put the following into it:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /code

COPY requirements.txt /code

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Then in our `docker-compose.yml` we need to add some entries under services:

```yml
  migration:
    container_name: migration
    build: ./backend
    command: /bin/sh -c "alembic upgrade head"
    environment:
      - DATABASE_URL=postgresql://postgres:password@database:5432/postgres
    depends_on:
      db:
        condition: service_healthy

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
```

## Connect to our Database

We need to add 2 imports to our `main.py`

```python
from contextlib import asynccontextmanager

from sqlalchemy import create_engine
```

Then add the following:

```python
DB_URL = "sqlite:///./app.db"

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(DB_URL)
    app.state.db = engine
    try:
        yield
    finally:
        engine.dispose()
```

The `DB_URL` should be whatever we put in for the value in our `alembic.ini`.

Then our app definition becomes:

```python
app = FastAPI(lifespan=lifespan)
```

## Dealing with CORS

In our `main.py` we need to add another import:

```python
from fastapi.middleware.cors import CORSMiddleware
```

Then add the following below the definition of our app:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Our First Controller

The first controller we will add is the users controller. We need a controller to register users and log in users. Let's make a folder called handlers in the backend folder.

In the handlers folder, add `user_handler.py` and to that add the following contents:

```python
from fastapi import APIRouter, Request

router = APIRouter(prefix="/user")

@router.post("/login")
async def login(request: Request):
    """
    Login a user
    """
    return {"message": "Login successful"}

@router.post("/register")
async def register(request: Request):
    """
    Register a new user
    """
    return {"message": "User registered"}
```

To connect this to the main app, we need to add the following line in `main.py` under the CORS middleware are set up.

```python
app.include_router(user_handler.router)
```

We'll also need to import the user_handler so we'll add the following import as well:

```python
from handlers import user_handler
```

### Finishing /register

First we need to make it take a username, email, and password, then we need to add it to the database or return an error if the email is already used.

First add the following imports:

```python
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
import hashlib

from models.models import User
```

Then above the `/register` endpoint add the following code to define the parameters required for the request:

```python
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
```

Lastly, let's update the function to require our body, check if there is a user with the email already, then if not create the user.

```python
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
```

### Finishing Login

For login we want to make the request take the email and password. Let's make a model for the request. 

```python
class LoginRequest(BaseModel):
    email: str
    password: str
```

We need to make a JWT here so let's add an import:

```python
import jwt
```

Then let's update the login function body to check if the user exists, if the password is correct, and then return a token for the user.

```python
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
```

## Post and Comment Models

We need to have a model for Community Posts and Comments. Let's go add the folllowing to our `models.py`. 

```python
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
```

Additionally, we need to add the following to the User model:

```python
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
```

We also need to add some imports. Add:

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
```

Then let's create a revision for this change in models by running:

```bash
alembic revision --autogenerate -m "Create Users and Posts"
```

If you are not using Docker, run:

```bash
alembic upgrade head
```

## Set Up the Post Controller

Make a file in handlers called `post_handler.py`. To it add the following:

```python
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from models.models import Post, Comment

from sqlalchemy.orm import Session

router = APIRouter(prefix="/post")

class CreatePostRequest(BaseModel):
    title: str
    content: str

@router.post("/")
async def create_post(request: Request, create_post_request: CreatePostRequest):
    """
    Create a post
    """
    
    with Session(request.app.state.db) as session:
        post = Post(
            title=create_post_request.title,
            content=create_post_request.content,
            user_id=1
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
async def create_comment(request: Request, create_comment_request: CreateCommentRequest):
    """
    Create a comment
    """
    
    with Session(request.app.state.db) as session:
        comment = Comment(
            content=create_comment_request.content,
            user_id=1,
            post_id=create_comment_request.post_id
        )
        session.add(comment)
        session.commit()

    return JSONResponse(
        status_code=200,
        content={"message": "Comment created"}
    )
```

We also need to add the post handler to our `main.py` we need to import the handler and then add it as a router.

Add the import:

```python
from handlers import user_handler, post_handler
```

Add the router:

```python
app.include_router(post_handler.router)
```

This sets up the creation for posts and comments, but it is flawed. We don't check that the user is logged in and we always use a user id of 1. 

### Checking Auth

Let's add a utils folder in our backend, then add a file called `auth.py`. To that file add:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def validate_token(token: str = Depends(oauth2_scheme)):
    token_data = jwt
    try:
        token_data = jwt.decode(token, "secret", algorithms=["HS256"])
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return token_data 
```

This will be used to decode and validate tokens. Let's add this to our endpoints.

Add the following import to the post handler:

```python
from fastapi import Depends
from utils.auth import validate_token
```

Then to both of our method signatures add:

```python
token_data: dict = Depends(validate_token)
```

Where we previously hard coded 1 for the user_id we can now use:

```python
token_data["user_id"]
```

Our post handler should now look like:

```python
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
```

### Get Post Endpoint

We need to be able to retrieve all the posts to display them.

To do this add the following to our post handler:

```python
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
```

# Coding the Frontend

## Expanding our gitignore

We used the python template for our gitignore when we made the repo, but now we need to add the relevant gitignore items for Node.js. To do that, let's copy the contents of [this file](https://github.com/github/gitignore/blob/main/Node.gitignore) and paste it to the bottom of our gitignore.

## Start our Sveltekit project

From the root of our git repo, run:

```bash
npx sv create frontend
```

In the creation options, select:
- SvelteKit Minimal
- Yes, using TypeScript syntax
- Tailwindcss
- The typography plugin
- npm

Enter the frontend folder and run:

```bash
npm install
```




